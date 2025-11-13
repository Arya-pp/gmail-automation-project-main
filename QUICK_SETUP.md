# 🚀 Quick Setup Guide - Gmail Credentials

## Step 1: Get Google Cloud Credentials

### 1. Go to Google Cloud Console

Visit: https://console.cloud.google.com/

### 2. Create a New Project (or select existing)

- Click on the project dropdown at the top
- Click "New Project"
- Name it: "Gmail Automation"
- Click "Create"

### 3. Enable Gmail API

- In the left sidebar, go to **"APIs & Services"** > **"Library"**
- Search for **"Gmail API"**
- Click on it and press **"Enable"**

### 4. Configure OAuth Consent Screen

- Go to **"APIs & Services"** > **"OAuth consent screen"**
- Select **"External"** (unless you have a workspace)
- Click **"Create"**

Fill in the required fields:

- **App name:** Gmail Automation
- **User support email:** Your email
- **Developer contact:** Your email
- Click **"Save and Continue"**

On Scopes page:

- Click **"Save and Continue"** (no changes needed)

On Test Users page:

- Click **"Add Users"**
- Add your Gmail address
- Click **"Save and Continue"**

### 5. Create OAuth 2.0 Credentials

- Go to **"APIs & Services"** > **"Credentials"**
- Click **"+ Create Credentials"** at the top
- Select **"OAuth client ID"**

Configure:

- Application type: **"Desktop app"**
- Name: **"Gmail Automation Desktop"**
- Click **"Create"**

### 6. Download Credentials JSON File

**IMPORTANT: You need to download the JSON file, not just copy the IDs**

After clicking "Create", you'll see a popup with Client ID and Client Secret.

**DO THIS:**

1. Click **"DOWNLOAD JSON"** button (small download icon at the bottom of the popup)
2. OR go back to **"Credentials"** page
3. Find your **"Gmail Automation Desktop"** in the list under "OAuth 2.0 Client IDs"
4. Click the **download icon** (↓) on the right side of your credential
5. A JSON file will download (named something like `client_secret_xxxxx.json`)

### 7. Rename and Move the File

**CRITICAL STEPS:**

1. Find the downloaded JSON file (usually in your Downloads folder)
2. **Rename it** to exactly: `credentials.json`
3. **Move it** to your project folder:
   ```
   C:\Users\91623\Downloads\gmail-automation-project-main\credentials.json
   ```

**PowerShell Commands (if file is in Downloads):**

```powershell
# Navigate to Downloads
cd $env:USERPROFILE\Downloads

# Find the file (look for client_secret*.json)
dir client_secret*.json

# Rename and move it (replace XXXXX with your actual filename)
Move-Item "client_secret_XXXXX.json" "C:\Users\91623\Downloads\gmail-automation-project-main\credentials.json"
```

**OR manually:**

- Open File Explorer
- Go to Downloads folder
- Find `client_secret_xxxxx.json`
- Right-click > Rename to `credentials.json`
- Cut and paste to: `C:\Users\91623\Downloads\gmail-automation-project-main\`

---

## Step 2: First Authentication

### Run the Gmail Script

Open PowerShell in your project folder and run:

```powershell
python gmail_automation.py
```

**What will happen:**

1. Your browser will automatically open
2. Sign in with your Google account
3. You'll see a warning: "Google hasn't verified this app"
   - Click **"Advanced"**
   - Click **"Go to Gmail Automation (unsafe)"**
4. Grant permissions by clicking **"Allow"**
5. The browser will show "The authentication flow has completed"
6. A `token.json` file will be created automatically

---

## Step 3: Verify Setup

### Check if files exist:

```powershell
# Check for credentials.json
dir credentials.json

# Check for token.json (after first run)
dir token.json
```

### Test the web app:

```powershell
python app.py
```

Then open: http://localhost:5000

---

## 📁 Expected File Structure

After setup, you should have:

```
gmail-automation-project-main/
├── credentials.json        ✅ (You downloaded this)
├── token.json             ✅ (Created after first auth)
├── .env                   ✅ (Contains GEMINI_API_KEY)
├── app.py
├── gmail_automation.py
└── templates/
    └── index.html
```

---

## 🐛 Troubleshooting

### "credentials.json not found"

- Make sure you downloaded the JSON file from Google Cloud Console
- Rename it to exactly `credentials.json` (not `client_secret_xxx.json`)
- Place it in the project root folder

### "Access blocked: This app's request is invalid"

- Make sure you added your email as a test user in OAuth consent screen
- Make sure Gmail API is enabled

### "token.json not found"

- This is normal on first run
- Run `python gmail_automation.py` to create it
- Follow the browser authentication flow

### Browser doesn't open automatically

- A URL will be printed in the terminal
- Copy and paste it into your browser manually

---

## ✅ Success Checklist

- [ ] Google Cloud project created
- [ ] Gmail API enabled
- [ ] OAuth consent screen configured
- [ ] Test user (your email) added
- [ ] OAuth credentials created and downloaded
- [ ] `credentials.json` in project folder
- [ ] Ran `python gmail_automation.py` successfully
- [ ] Completed browser authentication
- [ ] `token.json` file created
- [ ] Web app shows "Configuration complete"

---

## 🎉 Ready to Use!

Once setup is complete:

1. Run `python app.py`
2. Open http://localhost:5000
3. Click "Fetch Unread Emails"
4. Click "Summarize with AI"

Enjoy your Gmail Automation Dashboard!
