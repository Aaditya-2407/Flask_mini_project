# 📚 Flask MCQ Generator

Generate interactive multiple-choice quizzes from PDF documents using AI-powered extraction and processing.

---

## 🚀 Getting Started

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/Aaditya-2407/Flask_mini_project
cd Flask_mini_project
```

### 2. Set Up Virtual Environment

**On macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**On Windows:**

```cmd
python3 -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

1. Create a file named `.env` in the root folder
2. Get a free API Key from [Google AI Studio](https://makersuite.google.com/app/apikey)
3. Add your key to the `.env` file:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

### 5. Run the Application

```bash
python run.py
```

Open your browser and navigate to: **http://127.0.0.1:5000**

---

## 🛠️ How It Works

1. **Extraction**: Uses PyMuPDF (`fitz`) to read raw text from your PDF
2. **AI Processing**: Sends text to `gemini-1.5-flash` to generate a structured JSON object
3. **Frontend Rendering**: JavaScript parses the JSON to build an interactive quiz UI

---

## 📂 Project Structure

```
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
```

---

## 📋 Requirements

- Python 3.8+
- Flask
- PyMuPDF (fitz)
- Google Generative AI SDK
- python-dotenv

---

## 🔐 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Your Google AI Studio API key | Yes |

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---


## 👨‍💻 Author

**Aaditya Kharat**  
[GitHub Profile](https://github.com/Aaditya-2407)

---

## ⭐ Show Your Support

If you found this project helpful, please give it a ⭐ on GitHub!
