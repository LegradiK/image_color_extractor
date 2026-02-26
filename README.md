# Image Color Extractor (Flask App)

A simple web application built with Flask that allows users to upload an image and extract the most dominant colors from it. The app resizes the image, filters similar colors using a delta threshold, and returns the top most frequent distinct colors.

## Features

- Upload image files (png, jpg, jpeg, gif, webp)
- Automatically resizes images for consistent processing
- Extracts dominant colors
- Filters similar colors using Euclidean distance
- Adjustable:
    - Number of top colors
    - Color similarity threshold (delta)
- Displays processed image and extracted colors

## Tech Stack


**Backend / Language**  
- Python 3  
- Flask  
- Pillow (PIL)  
- Werkzeug  

**Frontend / UI**  
- HTML (Jinja templates)  
- Bootstrap 5 (CSS framework for responsive design and styling)  
- Bootstrap Icons (for info icons and other UI elements) 

## Project Structure

```bash
project/
│
├── main.py
├── .gitignore
├── LICENSE
├── static/
│   └── uploads/SAVE_YOUR_PICS_HERE
│   └── style.css
├── templates/
│   └── home.html
│   └── base.html 
│   └── header.html
│   └── footer.html
└── README.md
```

## Installation

1. Clone the repository
```bash
get clone https://github.com/LegradiK/image_color_extractor.git

cd into-your-repo-location
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install flask pillow werkzeug
```

## Running the App
```bash
python3 main.py
```
The application will start in debug mode:
```
http://127.0.0.1:5000/
```
Open the URL in your browser

### How it works
1. Image Upload

- Validates file extension.
- Resizes image to a base width of 600px while maintaining aspect ratio.

2. Color Extraction

- Reads pixel data from the image.
- Applies a <a href="https://en.wikipedia.org/wiki/Color_difference#Euclidean">Euclidean distance formula</a> to compare RGB values


3. Delta Filtering

- Filters out colors that are too similar based on a configurable threshold.
- Ensures distinct dominant colors.

4. Top Color Selection

- Counts color occurrences.
- Returns the top X most common filtered colors.

## Allowed File Extensions
```
png, jpg, jpeg, gif, webp
```
## Attribution

Icon used in this project are by [Freepik - Flaticon](https://www.flaticon.com/free-icons/info)
