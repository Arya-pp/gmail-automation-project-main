# ❌ FIX: Error 400: redirect_uri_mismatch

## 🔴 The Problem

Your OAuth credentials were created as **"Web application"** instead of **"Desktop app"**

---

## ✅ QUICK FIX - Delete and Recreate Credentials

### Step 1: Delete Current OAuth Credential

1. Go to: **https://console.cloud.google.com/apis/credentials**
2. Find your OAuth 2.0 Client ID (probably named "GmailAutomationDesktop" or similar)
3. Click the **trash/delete icon** (🗑️) on the right
4. Click **"DELETE"** to confirm

### Step 2: Create NEW Desktop App Credential

1. Still on the Credentials page
2. Click **"+ CREATE CREDENTIALS"** at the top
3. Select **"OAuth client ID"**

4. **IMPORTANT - Choose the RIGHT type:**
   - **Application type:** Select **"Desktop app"** ⬅️ MUST BE THIS!
   - **NOT** "Web application"
   - **NOT** "Android" or "iOS"
5. **Name:** `GmailDesktopApp`

6. Click **"CREATE"**

### Step 3: Download the NEW Credentials

1. Popup appears: "OAuth client created"
2. Click **"DOWNLOAD JSON"**
3. Save the file

### Step 4: Replace Old credentials.json

```powershell
# Delete old credentials.json
Remove-Item credentials.json

# Go to Downloads
cd $env:USERPROFILE\Downloads

# Find the new file
dir client_secret*.json

# Copy the newest one to project folder (replace XXXXX)
Copy-Item "client_secret*.json" "C:\Users\91623\Downloads\gmail-automation-project-main\credentials.json"
```

**OR manually:**

- Delete old `credentials.json` from project folder
- Find new `client_secret_xxx.json` in Downloads
- Rename to `credentials.json`
- Copy to project folder

### Step 5: Try Authentication Again

```powershell
# Make sure you're in the project folder
cd C:\Users\91623\Downloads\gmail-automation-project-main

# Delete old token
Remove-Item token.json -ErrorAction SilentlyContinue

# Try again
python gmail_automation.py
```

---

## 🎯 What to Look For When Creating Credentials:

When you click "Create OAuth client ID", you'll see a dropdown:

```
Application type:
[ Select... ▼ ]

Options:
  - Web application           ❌ WRONG
  - Android                   ❌ WRONG
  - Chrome app               ❌ WRONG
  - iOS                      ❌ WRONG
  - Desktop app              ✅ CORRECT! CHOOSE THIS!
  - Universal Windows Platform ❌ WRONG
```

**You MUST select: "Desktop app"**

---

## 🔍 How to Verify You Created Desktop App:

After creating, on the Credentials page, you should see:

```
OAuth 2.0 Client IDs

Name                Type           Creation date
GmailDesktopApp    Desktop app    Today         [↓] [🗑️]
                   ^^^^^^^^^^^
                   MUST say "Desktop app"
```

If it says "Web application", delete it and create again!

---

## 📸 Visual Check:

When creating credentials:

**WRONG (causes redirect_uri_mismatch):**

```
Application type: Web application
Authorized JavaScript origins: [...]
Authorized redirect URIs: [...]
```

**CORRECT (works!):**

```
Application type: Desktop app
Name: GmailDesktopApp
[No URIs to configure]
```

---

## ✅ Success Test

After fixing, run:

```powershell
python gmail_automation.py
```

You should see:

1. Browser opens
2. Sign in page (no error!)
3. "Google hasn't verified this app" warning (normal)
4. Allow permissions
5. Success!

---

## 💬 Still Having Issues?

Tell me:

- Did you select "Desktop app"?
- What does it say under "Type" on the Credentials page?
- Any new error messages?

I'll help! 🚀
