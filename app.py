import os
import tempfile
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import pytesseract
import pyttsx3
from PIL import Image
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/", methods=["POST"])
def upload_image():
    # Get the uploaded image file from the form
    image = request.files["image"]

    # Save the image file to a temporary directory
    image_path = os.path.join(tempfile.gettempdir(), secure_filename(image.filename))
    image.save(image_path)

    # Use Tesseract OCR to extract the text from the image
    text = pytesseract.image_to_string(Image.open(image_path))

    # Use pyttsx3 to speak the extracted text
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

    # Render the result template with the extracted text
    return render_template("result.html", text=text)


if __name__ == "__main__":
    app.run(debug=True)
