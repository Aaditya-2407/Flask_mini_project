🚀 Getting StartedFollow these steps to set up the project on your local machine.Step 1: Clone the RepositoryOpen your terminal and clone the project:Bashgit clone https://github.com/Aaditya-2407/Flask_mini_project
          cd Flask_mini_project
Step 2: Set Up Virtual EnvironmentIsolation is key! Create a virtual environment to manage your dependencies.Bash# Create the virtual environment
          python3 -m venv .venv

# Activate the virtual environment
# On macOS/Linux:
      source .venv/bin/activate
# On Windows:
      .venv\Scripts\activate
Step 3: Install DependenciesWith the environment active, install the required libraries:Bashpip install -r requirements.txt
Step 4: Configure Environment VariablesThe application requires an API key to communicate with the AI.Create a file named .env in the root folder.Visit Google AI Studio to get a free Gemini API Key.Add the following line to your .env file:PlaintextGEMINI_API_KEY=your_actual_api_key_here
Step 5: Run the ApplicationLaunch the Flask development server:Bashpython run.py
Open your browser and navigate to: http://127.0.0.1:5000🛠️ Project ArchitectureThis project is divided into logical steps to make learning easier:ComponentResponsibilityTechnologyFrontendSimple UI for file upload and question displayHTML5 / Vanilla JS (Fetch API)BackendAPI endpoints and file managementFlask (Python)ExtractorParsing text from binary PDF filesPyMuPDF (fitz)AI LogicPrompt engineering and MCQ generationGoogle Gemini 1.5 Flash📂 File StructurePlaintextFlask_mini_project/
├── app/
│   ├── templates/      # HTML frontend
│   ├── __init__.py     # App factory
│   └── routes.py       # Flask endpoints
├── uploads/            # Temporary storage for PDFs
├── extractor.py        # PDF text extraction logic
├── mcq.py              # Gemini AI integration
├── run.py              # Application entry point
├── .env                # API Keys (Secret)
└── requirements.txt    # Project dependencies
