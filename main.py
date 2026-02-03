import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
base_width = 600

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def home():
    image_url = None
    colors = None

    if request.method == "POST":
        file = request.files.get("image")
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
            print(colors)

    return render_template(
        "home.html",
        image_url=image_url,
        colors=colors
    )


if __name__ == '__main__':
    app.run(debug=True)