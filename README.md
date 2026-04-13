# 📝 PDF MCQ Generator

An AI-powered web application that transforms PDF documents into interactive Multiple Choice Questions. Built with **Flask** and **Google Gemini**, this project demonstrates a complete AI integration pipeline.

---

## 🚀 Getting Started

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/Aaditya-2407/Flask_mini_project](https://github.com/Aaditya-2407/Flask_mini_project)
cd Flask_mini_project
2. Set Up Virtual Environment
Isolation ensures that your dependencies don't conflict with other projects.

Bash
# Create the virtual environment
python3 -m venv .venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Configure API Keys
The application uses Google Gemini to generate questions.

Create a file named .env in the root folder.

Get a free API Key from Google AI Studio.

Add your key to the .env file:

Code snippet
GEMINI_API_KEY=your_actual_api_key_here
5. Run the Application
Bash
python run.py
Open your browser and navigate to: http://127.0.0.1:5000

🛠️ How It Works
Extraction: The app uses PyMuPDF to read the raw text from your uploaded PDF.

AI Processing: The text is sent to the gemini-1.5-flash model with instructions to return a structured JSON object.

Frontend Rendering: JavaScript parses the JSON and dynamically builds the quiz UI.

📂 Project Structure
Plaintext
Flask_mini_project/
├── app/
│   ├── templates/      # HTML UI files
│   ├── __init__.py     # Flask app factory
│   └── routes.py       # API endpoints
├── extractor.py        # PDF parsing logic
├── mcq.py              # Gemini AI integration
├── run.py              # Main entry point
├── .env                # API Keys (Git ignored)
└── requirements.txt    # Project dependencies
