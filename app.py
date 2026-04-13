from flask import Flask, request
from werkzeug.utils import secure_filename
from extractor import extract_text_from_pdf
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "Flask is working!"

@app.route("/upload", methods=["POST"])
def upload_pdf():
    file = request.files.get("pdf")

    if not file or file.filename == "":
        return {"error": "No PDF uploaded"}, 400

    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files allowed"}, 400

    filename = secure_filename(file.filename)
    path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(path)

    text = extract_text_from_pdf(path)

    return {
        "message": "PDF uploaded",
        "filename": filename,
        "text": text[:1000]
    }