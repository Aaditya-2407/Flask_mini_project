from flask import Flask ,request
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_pdf():
    file=request.files.get['pdf']

    if not file or file.filename == '':
        return "No file uploaded", 400
    
    if not file.filename.lower().endswith('.pdf'):
        return "Only PDF files are allowed", 400
    filename = secure_filename(file.filename)
    path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(path)
    return {"message": "PDF Uploaded", "filename": filename}, 200

@app.route('/')
def hello_world():
    
    return "Flask app is running!       "