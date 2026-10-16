# 🤖 AI Chat Reply Bot

An AI-powered chat automation project built with **Python** and the **Google Gemini API**. This project analyzes chat history, generates context-aware replies, and automates text input using PyAutoGUI.

The goal is to explore how generative AI can be combined with desktop automation to create an intelligent chat assistant.

## ✨ Features

- **AI-Powered Responses** — Generates replies using Google's Gemini API.
- **Context-Aware Conversations** — Uses copied chat history to generate relevant responses.
- **Automated Chat Interaction** — Uses PyAutoGUI to control mouse and keyboard actions.
- **Clipboard Integration** — Copies chat text and pastes generated responses using Pyperclip.
- **Sender Detection** — Checks whether the latest message belongs to a specified sender.
- **Custom AI Personality** — Supports a configurable personality and Hindi-English communication style.
- **Mouse Coordinate Detection** — Helps identify screen coordinates for desktop automation.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Google Gemini API | AI-generated responses |
| PyAutoGUI | Mouse and keyboard automation |
| Pyperclip | Clipboard operations |

## 📁 Project Structure

```text
AI-Chat-Reply-Bot/
│
├── cursor.py       # Chat reading, AI replies, and automation
├── bot.py          # Mouse coordinate detection
├── gemini api.py   # Gemini API response example
└── README.md       # Project documentation
```

## ⚙️ Requirements

- Python 3.10 or a compatible version
- A Google Gemini API key
- Internet connection
- A desktop computer with a graphical interface
- A supported chat application open on screen

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
cd YOUR_REPOSITORY_NAME
```

Replace the placeholders with your actual GitHub repository URL and repository folder name.

### 2. Install Dependencies

```bash
pip install pyautogui pyperclip google-genai
```

### 3. Configure the Gemini API Key

Set your API key as an environment variable named `GEMINI_API_KEY`.

**Windows PowerShell:**

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

Update the client configuration in your Python scripts:

```python
import os
from google import genai

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)
```

Replace the existing hardcoded API key configuration in both Gemini-related scripts.

**Security note:** Never commit your real API key to GitHub. Environment variables set this way in PowerShell apply to the current session.

### 4. Run the Project

Run the relevant script from your terminal:

```bash
python "gemini api.py"
```

To identify mouse coordinates:

```bash
python bot.py
```

To run the main chat automation:

```bash
python cursor.py
```

**Note:** The scripts have different purposes. Configure the screen coordinates and chat interface before running the automation script.

## 🔍 How It Works

1. **Read:** Selects and copies visible chat text.
2. **Detect:** Checks whether the latest copied message is from the configured sender.
3. **Analyze:** Sends the chat history to the Gemini API when the condition matches.
4. **Generate:** Receives an AI-generated reply.
5. **Paste:** Copies the generated response to the clipboard and pastes it into the chat input.
6. **Send:** Presses Enter to send the response automatically.

## 🔐 Privacy and Security

- Keep API keys and credentials private.
- Do not share confidential conversations without permission.
- Be aware that copied chat history may be sent to the Gemini API.
- Review AI-generated responses before sending them.
- Use the automation only in applications and contexts where you have permission.
- Test with sample conversations before using real chats.

## ⚠️ Limitations

- Depends on screen coordinates, which may vary across displays.
- Requires the target chat application to be open and positioned correctly.
- Sender detection depends on the formatting of the copied chat text.
- AI-generated responses may be inaccurate or inappropriate.
- Automatic sending can produce unintended messages if the wrong text is selected.

## 🔮 Future Improvements

- Add manual approval before sending replies.
- Improve chat parsing and sender identification.
- Add exception handling and configurable settings.
- Support different chat layouts and screen resolutions.
- Add safer logging and debugging options.
- Provide a simple graphical user interface.

## 👨‍💻 Author

**Aman**

Python Developer | Exploring AI, Automation, and Generative AI Applications

## ⚖️ Disclaimer

This project is intended for educational and experimental purposes. Use it responsibly and respect user privacy and the terms of service of third-party applications. The author is not responsible for misuse or unintended actions performed by the automation.

---

**Built with Python and Google Gemini AI.**
