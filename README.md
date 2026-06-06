# Mahakumbh BhashaSathi: Multilingual Pilgrim Companion

A practical, browser-based pilgrim assistant for Mahakumbh that helps visitors with navigation, event details, emergency support, accommodation guidance, local services, FAQs, and simple multilingual phrase translations.

## Project overview
- Project name: Mahakumbh BhashaSathi: Multilingual Pilgrim Companion
- Goal: Help first-time and returning pilgrims from diverse linguistic backgrounds navigate Mahakumbh with guidance, emergency support, local services, and multilingual phrase translation.
- Technology stack used:
  - Python 3.13
  - Standard library HTTP server
  - HTML, CSS, vanilla JavaScript
  - Local browser-based app architecture
- Note: This project does not use React, Next.js, Node.js, Django, Flask, FastAPI, MongoDB, PostgreSQL, or Flutter.
- AI-assisted development: The assistant logic and multilingual support were created using AI-assisted programming workflows for faster iteration and polished UX.

## Submission details
- GitHub repository: [Add your GitHub repo URL here]
- Deployment link: [Add deployed app URL here if available]
- Demo video / Loom link: [Add Loom link here]
- Presentation deck: Create slides covering problem, solution, features, architecture, demo, and future improvements.

## Project structure
- `maha_kumbh_assistant.py` — Local Python web server using only standard library modules.
- `static/index.html` — Responsive chat UI for pilgrim questions.
- `static/style.css` — Layout and visual styling.
- `static/app.js` — Front-end messaging logic and interaction helpers.
- `tests/test_assistant.py` — Unit tests for translation and answer selection.
- `requirements.txt` — Project dependency note.
- `run_server.bat` — Windows launch helper.
- `.gitignore` — Common ignored files.

## Features
- Navigation assistance for pilgrims.
- Event and ritual schedule guidance.
- Emergency contact advice and support tips.
- Accommodation and local service information.
- Multilingual phrase support for English, Hindi, Bengali, Gujarati, Marathi, Punjabi, Tamil, Telugu, Malayalam, Kannada, French, Japanese, and German.
- Built-in phrase translation logic and quick example prompts.

## Run locally
1. Open a terminal in `c:\dataset\maha_kumbh_assistant`.
2. Activate your virtual environment if needed.
3. Run the server with one of these commands:

```powershell
c:/dataset/.venv/Scripts/python.exe maha_kumbh_assistant.py
```

or if your virtual environment is activated:

```powershell
python maha_kumbh_assistant.py
```

4. Open `http://127.0.0.1:8080` in your browser.

### Windows quick launch
If your workspace contains the `.venv` folder one level above this project, run:

```powershell
run_server.bat
```

## Test locally
Run the unit tests from the project folder:

```powershell
python -m unittest discover tests
```

## Notes
- No external Python packages are required.
- The assistant is intentionally lightweight and offline-friendly.
- Use the language selector to choose the target translation language.

## Supporting materials for submission
- `README.md` with setup and run instructions.
- `tests/test_assistant.py` validating translation and answer selection.
- Local deployment instructions for running the app in a browser.
- Suggested demo script for video walkthrough.
- Suggested presentation deck outline.

## Next enhancements
- Add a richer multilingual phrase database.
- Integrate a small model or LLM endpoint for natural question answering.
- Add user location and navigation mapping support.
