# ❌ FIX: "Access blocked: gmail-automation's request is invalid"

## 🔴 The Problem

Your OAuth consent screen is missing required configuration or your email isn't added as a test user.

---

## ✅ SIMPLE FIX - Follow These Steps:

### Step 1: Go to OAuth Consent Screen

1. Open: **https://console.cloud.google.com/**
2. Select your project: **"Gmail Automation"**
3. Click the **☰ menu** (top left, 3 lines)
4. Go to: **"APIs & Services"** → **"OAuth consent screen"**

---

### Step 2: Add Required Scopes

This is the MOST IMPORTANT step!

1. Click **"EDIT APP"** button (top of the page)
2. Click **"SAVE AND CONTINUE"** on the first page
3. On the **"Scopes"** page:
   - Click **"ADD OR REMOVE SCOPES"**
   - In the search box, type: **gmail**
   - Find and check these boxes:
     - ✅ `.../auth/gmail.readonly` (Read emails)
     - ✅ `.../auth/userinfo.email` (See your email)
     - ✅ `.../auth/userinfo.profile` (See your profile)
   - Click **"UPDATE"** button at bottom
   - Click **"SAVE AND CONTINUE"**

---

### Step 3: Add Test User (YOUR EMAIL)

1. On the **"Test users"** page:
2. Click **"+ ADD USERS"**
3. Type YOUR Gmail address (the one you'll use to log in)
   - Example: `youremail@gmail.com`
4. Click **"ADD"**
5. Click **"SAVE AND CONTINUE"**
6. Click **"BACK TO DASHBOARD"**

---

### Step 4: Verify App Status

On the OAuth consent screen dashboard, you should see:

- ✅ Publishing status: **Testing**
- ✅ User type: **External**
- ✅ Test users: **1** (your email)

---

### Step 5: Download Credentials Again

Sometimes the credentials need to be re-downloaded after fixing OAuth:

1. Go to: **"APIs & Services"** → **"Credentials"**
2. Find your **"Gmail Automation Desktop"** OAuth 2.0 Client ID
3. Click the **download icon** (↓) on the right
4. Save the file
5. Rename it to: `credentials.json`
6. Replace the old one in your project folder:
   ```
   C:\Users\91623\Downloads\gmail-automation-project-main\credentials.json
   ```

---

### Step 6: Delete Old Token and Try Again

```powershell
# Delete old token (if it exists)
Remove-Item token.json -ErrorAction SilentlyContinue

# Try authenticating again
python gmail_automation.py
```

---

## 🎯 What Should Happen Now:

1. Browser opens automatically
2. You see: "Sign in with Google"
3. Choose your Gmail account
4. You might see: **"Google hasn't verified this app"**
   - This is NORMAL for testing
   - Click **"Advanced"**
   - Click **"Go to Gmail Automation (unsafe)"**
5. Click **"Allow"** to grant permissions
6. Browser shows: "The authentication flow has completed"
7. `token.json` is created ✅

---

## 🐛 Still Getting Error?

### Check These:

**1. Is Gmail API Enabled?**

```
APIs & Services → Library → Search "Gmail API" → Should show "MANAGE" (not "ENABLE")
```

**2. Is Your Email Added as Test User?**

```
OAuth consent screen → Test users → Should see your email
```

**3. Are Scopes Added?**

```
OAuth consent screen → Edit App → Scopes → Should see gmail.readonly
```

**4. Is App in Testing Mode?**

```
OAuth consent screen → Publishing status: Testing
```

---

## 📸 Visual Guide

When you're at **OAuth consent screen**, you should see:

```
📱 Gmail Automation
   Publishing status: ⚠️ Testing

   App information
   ├── App name: Gmail Automation
   ├── User support email: your@email.com
   └── Developer contact: your@email.com

   Scopes: 3 scopes
   ├── .../auth/gmail.readonly
   ├── .../auth/userinfo.email
   └── .../auth/userinfo.profile

   Test users: 1
   └── your@email.com
```

---

## ✅ Success Check

After completing all steps, run:

```powershell
python check_setup.py
```

This will verify everything is configured correctly!

---

## 💬 Need More Help?

Tell me at which step you're stuck and I'll give you more specific help!

Example:

- "I can't find OAuth consent screen"
- "I don't see ADD USERS button"
- "I added scopes but still getting error"

I'm here to help! 🚀
