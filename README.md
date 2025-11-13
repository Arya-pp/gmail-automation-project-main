# Gmail Automation Hub 📧✨# Gmail Automation Project 📧🤖

A modern web application for intelligent Gmail automation with AI-powered email summaries using **Google Gemini AI**.An intelligent Gmail automation tool with a **modern web interface** that fetches unread emails and provides AI-powered summaries using **Google Gemini AI**.

![Gmail Automation](https://img.shields.io/badge/Gmail-API-red)## ✨ New: Web Dashboard Available!

![Python](https://img.shields.io/badge/Python-3.7+-blue)

![Flask](https://img.shields.io/badge/Flask-3.0-green)This project now includes a beautiful, responsive web interface!

![Gemini](https://img.shields.io/badge/Gemini-AI-orange)

**Quick Start:**

## 🌟 Features

````bash

- 🌐 **Modern Web Dashboard** - Beautiful, responsive interface with Gmail-inspired designpython app.py

- 📧 **Gmail Integration** - Secure OAuth2 authentication```

- 🤖 **AI Summaries** - Powered by Google Gemini AI

- 📊 **Real-time Statistics** - Track unread and summarized emailsThen open http://localhost:5000 in your browser.

- 🎨 **Clean Email Display** - Automatic removal of tracking links and clutter

- 🔒 **Secure** - Environment-based configuration, no hardcoded secretsSee [WEB_APP_GUIDE.md](WEB_APP_GUIDE.md) for detailed web app documentation.



## 🚀 Quick Start## 🚀 Features



```bash- **🌐 Web Dashboard**: Modern, responsive web interface with real-time updates

# 1. Clone the repository- **Gmail Integration**: Securely connect to your Gmail account using OAuth2

git clone https://github.com/yourusername/gmail-automation-hub.git- **Email Fetching**: Automatically retrieve unread emails from your inbox

cd gmail-automation-hub- **AI Summarization**: Generate concise summaries using **Google Gemini AI** (formerly OpenAI)

- **Multi-format Support**: Handle both plain text and HTML emails

# 2. Install dependencies- **Error Handling**: Robust error handling for API calls and authentication

pip install -r requirements.txt- **Security**: Environment variable-based API key management

- **📊 Statistics Dashboard**: Track unread and summarized emails

# 3. Setup configuration- **💻 Command Line & Web Interface**: Use via terminal or web browser

cp .env.example .env

cp credentials.json.example credentials.json## 📋 Prerequisites



# 4. Add your API keys and credentials (see Configuration below)- Python 3.7+

- Gmail account

# 5. Run the web app- **Google Gemini API key** (Free tier available!)

python app.py- Google Cloud Console project with Gmail API enabled



# 6. Open browser## 🛠️ Installation

# Navigate to http://localhost:5000

```1. **Clone the repository**



## 📋 Prerequisites   ```bash

   git clone https://github.com/yourusername/gmail-automation-project.git

- **Python 3.7+**   cd gmail-automation-project

- **Gmail account**   ```

- **Google Gemini API key** ([Get it free](https://aistudio.google.com/app/apikey))

- **Google Cloud Console project** with Gmail API enabled2. **Install required packages**



## ⚙️ Configuration   ```bash

   pip install -r requirements.txt

### 1. Get Gemini API Key (2 minutes)   ```



1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)3. **Set up environment variables**

2. Click **"Create API Key"**

3. Copy the key   ```bash

4. Add to `.env` file:   # Copy the example file

   ```   cp .env.example .env

   GEMINI_API_KEY=your_api_key_here

   ```   # Edit .env and add your Gemini API key

   # GEMINI_API_KEY=your_gemini_api_key_here

### 2. Setup Gmail OAuth (5 minutes)   ```



**Detailed guides available:**4. **Get Gemini API Key**

- 📘 [QUICK_SETUP.md](QUICK_SETUP.md) - Fast setup guide   - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)

- 📗 [FRESH_START_GUIDE.md](FRESH_START_GUIDE.md) - Complete step-by-step   - Click "Create API Key"

- 📙 [FIX_ACCESS_BLOCKED_SIMPLE.md](FIX_ACCESS_BLOCKED_SIMPLE.md) - Troubleshooting   - Copy and paste into your `.env` file



**Quick steps:**## ⚙️ Configuration



1. Go to [Google Cloud Console](https://console.cloud.google.com/)### Gmail API Setup

2. Create new project or select existing

3. Enable **Gmail API**1. **Create Google Cloud Project**

4. Configure **OAuth consent screen**:

   - User type: External   - Go to [Google Cloud Console](https://console.cloud.google.com/)

   - Add your email as test user   - Create a new project or select existing one

   - Add required scopes: `gmail.readonly`

5. Create **OAuth 2.0 Client ID** (Desktop app)2. **Enable Gmail API**

6. Download JSON and save as `credentials.json`

   - Navigate to "APIs & Services" > "Library"

### 3. First Run Authentication   - Search for "Gmail API" and enable it



```bash3. **Configure OAuth Consent Screen**

python gmail_automation.py

```   - Go to "APIs & Services" > "OAuth consent screen"

   - Choose "External" user type

- Browser opens automatically   - Fill in required fields and add your email as a test user

- Sign in with your Gmail

- Click **Advanced** → **Go to app (unsafe)**4. **Create Credentials**

- Grant permissions   - Go to "APIs & Services" > "Credentials"

- `token.json` is created ✅   - Create "OAuth 2.0 Client ID" for Desktop application

   - Download the JSON file and save as `credentials.json`

## 🏃 Usage

### Gemini API Setup

### Start Web Application

1. Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

```bash2. Add it to your `.env` file as `GEMINI_API_KEY=your_key_here`

python app.py

```## 🏃‍♂️ Usage



Or on Windows:### Web Dashboard (Recommended!)

```bash

run_web.bat```bash

```# Start the web server

python app.py

Visit: **http://localhost:5000**

# Or use the batch file on Windows

### Web Dashboard Actionsrun_web.bat

````

1. **📬 Fetch Unread Emails** - Get latest unread emails from Gmail

2. **✨ Summarize with AI** - Generate AI summaries using GeminiThen open your browser to: **http://localhost:5000**

3. **🗑️ Clear All** - Remove all emails from dashboard

### Basic Email Fetching (Command Line)

### Command Line Usage

````bash

```bashpython gmail_automation.py

# Fetch emails only```

python gmail_automation.py

### Email Summarization

# Fetch and summarize

python email_summarizer.py```bash

```python email_summarizer.py

````

## 📁 Project Structure

### Setup Helper

````

gmail-automation-hub/```bash

│python setup.py

├── app.py                      # Flask web server```

├── gmail_automation.py         # Gmail API integration

├── email_summarizer.py         # Gemini AI summarization## 📁 Project Structure

├── requirements.txt            # Python dependencies

│```

├── templates/gmail-automation-project/

│   └── index.html             # Web dashboard UI│

│├── app.py                   # Flask web application

├── .env.example               # Environment template├── templates/

├── credentials.json.example   # OAuth credentials template│   └── index.html          # Web dashboard UI

│├── gmail_automation.py      # Core Gmail API functionality

├── run_web.bat               # Windows launcher├── email_summarizer.py      # AI-powered email summarization (Gemini)

│├── setup.py                 # Setup helper script

├── README.md                 # You are here!├── fix_oauth.py            # OAuth troubleshooting helper

├── QUICK_SETUP.md           # Fast setup guide├── test_setup.py           # Configuration test script

├── FRESH_START_GUIDE.md     # Detailed setup├── requirements.txt        # Python dependencies

├── FIX_ACCESS_BLOCKED_SIMPLE.md  # Troubleshooting├── .env.example           # Environment variables template

├── HOW_TO_RUN.md            # Running instructions├── run_web.bat            # Windows launcher for web app

└── WEB_APP_GUIDE.md         # Web app documentation├── WEB_APP_GUIDE.md       # Web application documentation

```├── GMAIL_SETUP_GUIDE.md   # Detailed setup instructions

├── set_api_key.bat        # Windows batch file for API key setup

## 🎨 Features in Detail└── README.md              # This file

````

### Clean Email Display

- Automatically removes tracking URLs## 🔧 Troubleshooting

- Strips HTML formatting

- Shows readable plain text### Common Issues

- Truncates very long emails

1. **OAuth Error 403**: Follow the detailed guide in `GMAIL_SETUP_GUIDE.md`

### AI Summarization2. **Gemini API Key Issues**: Ensure your API key is correctly set in `.env`

- Uses Google Gemini 1.5 Flash3. **Import Errors**: Make sure all dependencies are installed via `requirements.txt`

- Concise 2-3 sentence summaries4. **Web App Won't Start**: Run `pip install flask flask-cors`

- Key information extraction

- Free tier available### Helper Scripts

### Responsive Design- `fix_oauth.py`: Cleans up OAuth tokens and guides through re-authentication

- Professional grey/white color scheme- `test_setup.py`: Verifies your configuration setup

- Works on desktop, tablet, mobile- `setup.py`: Interactive setup assistant

- Gmail-inspired interface

- Smooth animations## 🛡️ Security Notes

## 🔧 Troubleshooting- Never commit your `.env` file or `credentials.json` to version control

- Use environment variables for sensitive data

| Issue | Solution |- Your Gmail app remains in "testing" mode - only you can access it

|-------|----------|- API keys and tokens are stored locally

| **Error 403: access_denied** | Add your email as test user in OAuth consent screen |- **Web app runs locally** - not exposed to the internet by default

| **redirect_uri_mismatch** | Use Desktop app credentials (not Web app) |

| **Missing credentials.json** | Download from Google Cloud Console |## 📝 Example Output

| **Gemini API error** | Check `.env` file has correct `GEMINI_API_KEY` |

| **Module not found** | Run `pip install -r requirements.txt` |```

🔍 Fetching unread emails...

**Detailed fixes:** See [FIX_ACCESS_BLOCKED_SIMPLE.md](FIX_ACCESS_BLOCKED_SIMPLE.md)📬 Found 3 unread emails

## 🛡️ Security & Privacy📧 Email #1

From: example@company.com

✅ **All data stays local** - No external servers Subject: Project Update

✅ **OAuth 2.0** - Secure Gmail authentication Date: Mon, 01 Jul 2025 10:30:00 GMT

✅ **Environment variables** - No hardcoded secrets Summary:

✅ **Testing mode** - Only you can access the app The project is on track for completion by the end of the week.

✅ **Read-only** - App only reads emails (gmail.readonly scope) The team has resolved the critical bugs and is now focusing on

final testing and documentation.

**Never commit:**------------------------------------------------------------

- `credentials.json` ❌```

- `token.json` ❌

- `.env` ❌## 🤝 Contributing

These files are in `.gitignore` for your protection!1. Fork the repository

2. Create a feature branch (`git checkout -b feature/amazing-feature`)

## 📦 Dependencies3. Commit your changes (`git commit -m 'Add amazing feature'`)

4. Push to the branch (`git push origin feature/amazing-feature`)

```5. Open a Pull Request

flask==3.0.3

flask-cors==6.0.1## 📄 License

google-auth-oauthlib==1.2.0

google-auth-httplib2==0.2.0This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

google-api-python-client==2.116.0

google-generativeai==0.8.5## ⚠️ Disclaimer

beautifulsoup4==4.12.3

python-dotenv==1.0.1This tool is for educational and personal use. Ensure you comply with Gmail's Terms of Service and Google's AI usage policies. Be mindful of API rate limits and costs (Gemini has a generous free tier!).

```

## 🙏 Acknowledgments

## 🤝 Contributing

- [Google Gmail API](https://developers.google.com/gmail/api)

Contributions welcome! Please:- [Google Gemini AI](https://ai.google.dev/)

- [Flask Web Framework](https://flask.palletsprojects.com/)

1. Fork the repository- [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/) for HTML parsing

2. Create feature branch (`git checkout -b feature/amazing`)

3. Commit changes (`git commit -m 'Add amazing feature'`)## 🆕 What's New

4. Push to branch (`git push origin feature/amazing`)

5. Open Pull Request- ✨ **Web Dashboard**: Beautiful, modern web interface

- 🤖 **Switched to Gemini AI**: Using Google's Gemini instead of OpenAI

## 📄 License- 📊 **Real-time Statistics**: Track your email management

- 🎨 **Responsive Design**: Works on all devices

MIT License - see [LICENSE](LICENSE) file- 🚀 **One-Click Launch**: Easy batch file to start the web app

## 🙏 Credits---

- [Google Gmail API](https://developers.google.com/gmail/api)Made with ❤️ for email automation

- [Google Gemini AI](https://ai.google.dev/)
- [Flask](https://flask.palletsprojects.com/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

## ⭐ Star This Repo!

If you find this project helpful, please give it a star! ⭐

---

**Made with ❤️ by [Your Name]**

📧 Questions? Open an issue!  
🐛 Found a bug? Report it!  
💡 Have an idea? Share it!
