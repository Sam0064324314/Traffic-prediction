# ⚡ Quick Git Commands Cheatsheet

Fast reference for pushing your project to GitHub. Complete details in `GITHUB_SETUP.md`.

---

## 🚀 Push to GitHub (30 seconds)

```bash
# 1. Navigate to project directory
cd C:\Users\jains\OneDrive\Desktop\Trffic

# 2. Initialize git (first time only)
git init

# 3. Configure git (first time only - use your actual name/email)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 4. Add all files
git add .

# 5. Create initial commit
git commit -m "Initial commit: Traffic Volume Prediction Dashboard with sklearn Pipelines"

# 6. Add GitHub remote (replace YOUR-USERNAME)
git remote add origin https://github.com/YOUR-USERNAME/traffic-volume-prediction.git

# 7. Push to GitHub
git push -u origin main

# Done! Check https://github.com/YOUR-USERNAME/traffic-volume-prediction
```

---

## 📋 Before Running Commands

1. ✅ Create GitHub account at https://github.com
2. ✅ Create new repository at https://github.com/new
3. ✅ Copy your repository HTTPS URL
4. ✅ Replace `YOUR-USERNAME` in the commands above

---

## 📝 Essential Commands

### Check Status
```bash
git status                    # See what's staged/untracked
git log                       # View commit history
git remote -v                 # View connected remotes
```

### Update Repository (after first push)
```bash
git add .
git commit -m "Your commit message"
git push origin main
```

### Pull Latest Changes
```bash
git pull origin main
```

---

## 🔑 First-Time Setup (One-Time)

```bash
# Configure your identity globally (do once)
git config --global user.name "Your Full Name"
git config --global user.email "your.email@example.com"

# Verify configuration
git config --global --list
```

---

## ⚠️ Troubleshooting Quick Fixes

**"fatal: remote origin already exists"**
```bash
git remote remove origin
git remote add origin https://github.com/YOUR-USERNAME/traffic-volume-prediction.git
```

**"Authentication failed"**
```bash
# Use HTTPS instead of SSH
git remote set-url origin https://github.com/YOUR-USERNAME/traffic-volume-prediction.git
# Then use Personal Access Token as password (see GITHUB_SETUP.md)
```

**".gitignore not working"**
```bash
git rm --cached *.pkl
git commit -m "Remove cached files"
git push origin main
```

---

## ✅ Verify on GitHub

1. Go to https://github.com/YOUR-USERNAME/traffic-volume-prediction
2. Check files are uploaded (except *.pkl and test_data.csv)
3. README.md should be visible
4. Commits should appear in history

---

## 📚 For Complete Guide
See `GITHUB_SETUP.md` for detailed explanations and advanced options.

---

**Ready to push? Run the commands above! 🚀**
