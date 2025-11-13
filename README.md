# Gmail Automation 📧

AI-powered Gmail automation with modern web interface using Google Gemini.

## ✨ Features

- 🌐 **Modern Web Dashboard** - Responsive interface with real-time updates
- 📧 **Search & Filter** - By sender, subject, and category (Social, Promotions, Updates)
- ✅ **Mark as Read/Unread** - Bulk and individual email management
- 📄 **Pagination** - Configurable results per page (5/10/20/50)
- 🤖 **AI Summaries** - Google Gemini generates concise email summaries
- 🎨 **Clean Display** - Automatic removal of tracking URLs and spam links

## 🛠️ Tech Stack

**Backend:**

- Python 3.11
- Flask 3.0.3
- Gmail API
- Google Gemini AI (gemini-2.0-flash)

**Key Libraries:**

- `google-auth-oauthlib` - OAuth 2.0 authentication
- `google-api-python-client` - Gmail API integration
- `google-generativeai` - Gemini AI SDK
- `beautifulsoup4` - HTML parsing and cleaning
- `python-dotenv` - Environment configuration

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Visit: **http://localhost:5000**

## ⚙️ Setup

### 1. Get Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click "Create API Key"
3. Add to `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

### 2. Setup Gmail OAuth

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create new project
3. Enable **Gmail API**
4. Configure **OAuth consent screen** (External, add your email as test user)
5. Create **OAuth 2.0 Client ID** (Desktop application)
6. Download JSON and save as `credentials.json`

**Detailed Setup Guides:**

- [QUICK_SETUP.md](QUICK_SETUP.md) - Fast setup guide
- [FRESH_START_GUIDE.md](FRESH_START_GUIDE.md) - Complete walkthrough
- [FIX_ACCESS_BLOCKED_SIMPLE.md](FIX_ACCESS_BLOCKED_SIMPLE.md) - Troubleshooting

## 📖 Usage

### Web Interface

```bash
python app.py
# Open http://localhost:5000 in your browser
```

**Features:**

- Fetch emails with pagination
- Search by sender or subject
- Filter by category
- Mark as read/unread
- Generate AI summaries

### Command Line

```bash
# Fetch emails only
python gmail_automation.py

# Fetch and summarize
python email_summarizer.py
```

## 🔧 Troubleshooting

| Issue                        | Solution                                            |
| ---------------------------- | --------------------------------------------------- |
| **Error 403: access_denied** | Add your email as test user in OAuth consent screen |
| **redirect_uri_mismatch**    | Use Desktop app credentials (not Web app)           |
| **Gemini API error**         | Check `.env` file has correct `GEMINI_API_KEY`      |
| **Rate limit 429**           | Wait a few minutes, auto-retry enabled              |

See [FIX_ACCESS_BLOCKED_SIMPLE.md](FIX_ACCESS_BLOCKED_SIMPLE.md) for detailed fixes.

## 🛡️ Security

✅ All data stays local  
✅ OAuth 2.0 secure authentication  
✅ Environment variables for secrets  
✅ Protected by `.gitignore`: `.env`, `credentials.json`, `token.json`

**Never commit these files:**

- `credentials.json`
- `token.json`
- `.env`

## 📁 Project Structure

```
gmail-automation-project/
├── app.py                   # Flask web server
├── gmail_automation.py      # Gmail API integration
├── email_summarizer.py      # AI summarization
├── templates/
│   └── index.html          # Web dashboard UI
├── requirements.txt         # Python dependencies
├── .env                    # API keys (not in repo)
├── credentials.json        # OAuth credentials (not in repo)
└── README.md               # This file
```

**Made with ❤️ for email automation**
