📚 Flask MCQ Generator
Generate interactive multiple-choice quizzes from PDF documents using AI-powered extraction and processing.

🚀 Getting Started
Follow these steps to set up the project on your local machine.
1. Clone the Repository
bashgit clone https://github.com/Aaditya-2407/Flask_mini_project
cd Flask_mini_project
2. Set Up Virtual Environment
On macOS/Linux:
bashpython3 -m venv .venv
source .venv/bin/activate
On Windows:
cmdpython3 -m venv .venv
.venv\Scripts\activate
3. Install Dependencies
bashpip install -r requirements.txt
4. Configure API Keys

Create a file named .env in the root folder
Get a free API Key from Google AI Studio
Add your key to the .env file:

plaintextGEMINI_API_KEY=your_actual_api_key_here
5. Run the Application
bashpython run.py
Open your browser and navigate to: http://127.0.0.1:5000

🛠️ How It Works

Extraction: Uses PyMuPDF (fitz) to read raw text from your PDF
AI Processing: Sends text to gemini-1.5-flash to generate a structured JSON object
Frontend Rendering: JavaScript parses the JSON to build an interactive quiz UI


📂 Project Structure
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

📋 Requirements

Python 3.8+
Flask
PyMuPDF (fitz)
Google Generative AI SDK
python-dotenv


🔐 Environment Variables
VariableDescriptionRequiredGEMINI_API_KEYYour Google AI Studio API keyYes
