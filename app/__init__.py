import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Configure upload folder
    app.config['UPLOAD_FOLDER'] = 'uploads'
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Register Blueprint
    from .routes import bp
    app.register_blueprint(bp)

    return app
