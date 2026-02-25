import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from PIL import Image
from collections import Counter
import math

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
base_width = 600

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# Calculate Euclidean distance between two colors
def color_distance(c1, c2):
    return math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2)

# Filter colors by delta threshold
def filter_colors(colors, delta_threshold):
    filtered = []
    for color in colors:
        if all(color_distance(color, f) > delta_threshold for f in filtered):
            filtered.append(color)
    return filtered

@app.route("/", methods=["GET", "POST"])
def home():
    image_url = None
    colors = None
    top_colors_list = []

    if request.method == "POST":
        file = request.files.get("image")
        top_x = int(request.form.get("num_colors", 5))
        delta = int(request.form.get("delta_colors", 30))
        image = Image.open(file)
        width_percent = (base_width / float(image.size[0]))
        height_size = int((float(image.size[1]) * float(width_percent)))
        image = image.resize((base_width, height_size), Image.Resampling.LANCZOS)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            image.save(filepath)

            image_url = url_for("static", filename=f"uploads/{filename}")

            image.save(filepath)

            image_url = url_for(
                "static",
                filename=f"uploads/{filename}"
            )

            colors = image.getdata()
            color_counts = Counter(colors)
            # Apply delta filter
            distinct_colors = filter_colors(color_counts, delta)
            ##### start from here ######
            top_colors = color_counts.most_common(top_x)
            for i in top_colors:
                top_colors_list.append(i[0])

        return render_template(
            "home.html",
            image_url=image_url,
            colors=colors,
            top_colors=top_colors_list
        )
    
    else:

        return render_template("home.html")




if __name__ == '__main__':
    app.run(debug=True)