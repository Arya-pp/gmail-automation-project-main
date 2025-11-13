# 🔄 Complete Fresh Start - Gmail OAuth Setup

## Step 1: Clean Up Old Setup

Run these commands to delete old credentials:

```powershell
# Delete old credentials files
Remove-Item credentials.json -ErrorAction SilentlyContinue
Remove-Item token.json -ErrorAction SilentlyContinue

# Confirm they're deleted
dir *.json
```

---

## Step 2: Delete Old Project in Google Cloud (Optional but Recommended)

1. Go to: **https://console.cloud.google.com/**
2. Click the **project dropdown** at the top (shows current project name)
3. Click **"Gmail Automation"** if you see it
4. Click the **3 dots menu** (⋮) next to the project name
5. Click **"Delete"**
6. Type the project ID to confirm
7. Click **"DELETE"**

---

## Step 3: Create Brand New Project

1. Still at: **https://console.cloud.google.com/**
2. Click the **project dropdown** at the top
3. Click **"NEW PROJECT"** (top right of the popup)
4. Fill in:
   - **Project name:** `gmail-automation-2025`
   - **Location:** Leave as default
5. Click **"CREATE"**
6. Wait 30 seconds for it to be created
7. **Select the new project** (make sure it's active)

---

## Step 4: Enable Gmail API

1. Click **☰ menu** (top left)
2. Go to: **"APIs & Services"** → **"Library"**
3. In the search box, type: **Gmail API**
4. Click on **"Gmail API"**
5. Click **"ENABLE"** button
6. Wait for it to enable (5-10 seconds)

---

## Step 5: Configure OAuth Consent Screen (Fresh Start)

1. Click **☰ menu** → **"APIs & Services"** → **"OAuth consent screen"**

2. **Choose User Type:**

   - Select: **"External"**
   - Click **"CREATE"**

3. **Edit app registration - Page 1 (App information):**

   Fill in these fields:

   - **App name:** `Gmail Automation Hub`
   - **User support email:** Select your email from dropdown
   - **App logo:** Leave blank
   - **App domain:** Leave blank
   - **Authorized domains:** Leave blank
   - **Developer contact information:** Type your email

   Click **"SAVE AND CONTINUE"**

4. **Page 2 (Scopes) - IMPORTANT:**

   - Click **"ADD OR REMOVE SCOPES"**
   - In the filter box at the top, type: `gmail`
   - Find and **CHECK** these boxes:
     - ☑️ `.../auth/gmail.readonly` (View your email messages and settings)
   - Click **"UPDATE"** at the bottom
   - You should see **"1 scope"** or **"1 sensitive scope"** added
   - Click **"SAVE AND CONTINUE"**

5. **Page 3 (Test users) - CRITICAL:**

   - Click **"+ ADD USERS"**
   - Type YOUR Gmail email address (the one you'll use)
   - Click **"ADD"**
   - You should see your email in the list
   - Click **"SAVE AND CONTINUE"**

6. **Page 4 (Summary):**

   - Review everything
   - Click **"BACK TO DASHBOARD"**

---

## Step 6: Create New OAuth Credentials

1. Click **☰ menu** → **"APIs & Services"** → **"Credentials"**

2. Click **"+ CREATE CREDENTIALS"** at the top

3. Select **"OAuth client ID"**

4. **If asked to configure consent screen:**

   - You already did this, so skip
   - If forced, click through quickly

5. **Create OAuth client ID:**

   - **Application type:** Select **"Desktop app"**
   - **Name:** `GmailAutomationDesktop`
   - Click **"CREATE"**

6. **Download the Credentials:**
   - A popup appears: "OAuth client created"
   - Click **"DOWNLOAD JSON"** button
   - The file downloads (named like `client_secret_123...json`)
   - Click **"OK"** to close popup

---

## Step 7: Move and Rename Credentials File

```powershell
# Go to Downloads folder
cd $env:USERPROFILE\Downloads

# List all client_secret files
dir client_secret*.json

# Copy the latest one to your project (replace XXXXX with actual filename)
Copy-Item "client_secret*.json" "C:\Users\91623\Downloads\gmail-automation-project-main\credentials.json"

# Verify it's there
cd C:\Users\91623\Downloads\gmail-automation-project-main
dir credentials.json
```

**OR do it manually:**

- Open File Explorer → Downloads folder
- Find `client_secret_xxxxx.json` (newest file)
- Copy it to: `C:\Users\91623\Downloads\gmail-automation-project-main\`
- Rename to: `credentials.json`

---

## Step 8: First Authentication

```powershell
# Make sure you're in the project folder
cd C:\Users\91623\Downloads\gmail-automation-project-main

# Run the authentication
python gmail_automation.py
```

**What happens:**

1. Browser opens automatically
2. Sign in with your Gmail
3. You see: **"Google hasn't verified this app"** ← This is NORMAL!
   - Click **"Advanced"**
   - Click **"Go to Gmail Automation Hub (unsafe)"**
4. Review permissions
5. Click **"Allow"**
6. Browser says: "The authentication flow has completed. You may close this window."
7. Terminal shows: "Authentication successful!"
8. `token.json` is created ✅

---

## Step 9: Test Everything

```powershell
# Check files exist
dir credentials.json
dir token.json

# Test the app
python app.py
```

Open browser to: **http://localhost:5000**

You should see: **✅ Configuration complete - Ready to use!**

---

## 🎯 Checklist - Complete Each Step:

- [ ] Delete old credentials.json and token.json
- [ ] Create new Google Cloud project: `gmail-automation-2025`
- [ ] Enable Gmail API
- [ ] Configure OAuth consent screen (External)
- [ ] Add scope: `gmail.readonly`
- [ ] Add test user: YOUR email address
- [ ] Create OAuth Desktop credentials
- [ ] Download and rename JSON to `credentials.json`
- [ ] Move to project folder
- [ ] Run `python gmail_automation.py`
- [ ] Complete browser authentication
- [ ] See `token.json` created
- [ ] Run `python app.py` and test

---

## 💬 Need Help?

At which step are you stuck? Tell me:

- Step number
- What you see on the screen
- Any error messages

I'll help you through it! 🚀
