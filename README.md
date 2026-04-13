🚀 Getting Started

Follow these steps to set up the project on your local machine.

1. Clone the Repository

git clone [https://github.com/Aaditya-2407/Flask_mini_project](https://github.com/Aaditya-2407/Flask_mini_project)
cd Flask_mini_project


2. Set Up Virtual Environment

# Create the virtual environment
python3 -m venv .venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate


3. Install Dependencies

pip install -r requirements.txt


4. Configure API Keys

Create a file named .env in the root folder.

Get a free API Key from Google AI Studio.

Add your key to the .env file:

GEMINI_API_KEY=your_actual_api_key_here


5. Run the Application

python run.py


Open your browser and navigate to: http://127.0.0.1:5000

🛠️ How It Works

Extraction: Uses PyMuPDF (fitz) to read raw text from your PDF.

AI Processing: Sends text to gemini-1.5-flash to generate a JSON object.

Frontend Rendering: JavaScript parses the JSON to build the quiz UI.

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
