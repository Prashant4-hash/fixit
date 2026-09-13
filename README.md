# FixIt CLI

> **Documentation:** [View Technical Project Documentation (.docx)](https://github.com/Prashant4-hash/fixit/blob/main/FixIt_CLI_Project_Documentation.docx)

An AI-powered terminal error helper built with Python and OpenRouter.

## Features
- Direct error string evaluation (ixit "git comit")
- Automatic terminal error stream piping (python script.py 2>&1 | fixit)
- Interactive execution prompt before running suggested commands

## Installation & Setup
1. **Clone Repository:** git clone https://github.com/Prashant4-hash/fixit.git
2. **Store API Credentials:** Create key.txt inside the project folder and paste an OpenRouter API key.
3. **Register PowerShell Function:** Append the ixit function into $PROFILE using Add-Content.
4. **Verify Setup:** Run ixit "git comit" to confirm live AI responses.