import os
import json
from flask import Blueprint, current_app, render_template, request
from werkzeug.utils import secure_filename
from app.services.extractor import extract_text_from_pdf
from app.services.mcq import generate_mcqs

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/upload", methods=["POST"])
def upload_pdf():
    file = request.files.get("pdf")
    if not file:
        return {"error": "No file uploaded"}, 400

    filename = secure_filename(file.filename)
    path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    file.save(path)

    try:
        text = extract_text_from_pdf(path)
        
        raw_questions_str = generate_mcqs(text)
        
        if isinstance(raw_questions_str, str):
            questions_dict = json.loads(raw_questions_str)
        else:
            questions_dict = raw_questions_str
            
        if 'questions' in questions_dict:
            return questions_dict
        else:
            return {"questions": questions_dict}

    except Exception as e:
        return {"error": str(e)}, 500
