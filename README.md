# GitHub Contributions Booster 🚀

**Author:** [Mr-Risov](https://github.com/Mr-Risov)  
**Description:** This script automatically generates **unlimited folders** inside a private repository, each containing **1,000 files**, to increase GitHub contributions.

---

## 📌 Features

✅ Creates **infinite folders** (`folder_1`, `folder_2`, ...)  
✅ Each folder contains **1,000 random text files**  
✅ Commits & pushes files automatically to your GitHub repo  
✅ Works with **private repositories**  
✅ Bypasses the **GitHub contribution system's display limit**  

---

## 📝 Installation Guide

### 1️⃣ Clone This Repository  
```bash
git clone https://github.com/Mr-Risov/GitHub-Contributions-Booster.git
cd GitHub-Contributions-Booster
```

### 2️⃣ Install Required Dependencies  
```bash
pip install -r requirements.txt
```

## ▶️ Usage

Run the script to start generating **unlimited files & folders**:

```bash
python script.py
```

> ⚠️ **Note**: The script will run **continuously**, creating folders and files until manually stopped.
> 

### 3️⃣ Get Your GitHub API Key  
1. Go to **[GitHub Developer Settings](https://github.com/settings/tokens)** → **Personal Access Tokens**  
2. Click **"Generate new token (classic)"**  
3. Enable the following **scopes**:  
   - ✅ `repo` (Full control of private repositories)  
   - ✅ `workflow` (GitHub Actions, optional)  
4. Copy the token and save it securely.  

---

## 🔧 Configuration

Auto Create a `config.json` file to store your GitHub API details:

```json
{
    "GITHUB_API_KEY": "your_personal_access_token",
    "REPO_OWNER": "your_github_username",
    "REPO_NAME": "your_repository_name"
}
```

---

## 🔄 How Does It Work?

1. The script **creates a new folder** (e.g., `folder_1`, `folder_2`, `folder_3`...)
2. Inside each folder, it **creates 1,000 files** (`file_1.txt`, `file_2.txt`, etc.)
3. Commits and **pushes** the changes to your **GitHub repository**
4. Repeats **infinitely** until you **stop the script**

---

## ⚠️ Important Considerations

- **GitHub API Rate Limit:** Max **5,000 requests per hour** (script has built-in delay to prevent blocking).
- **Repository Size:** Avoid making the repo too large or GitHub might throttle the updates.
- **Private Contributions:** Ensure **“Include private contributions”** is enabled in GitHub **profile settings**.

---

## 💡 Use Cases

✅ **Boost your GitHub contributions** for a strong profile  
✅ **Automate commits** to private repositories  
✅ **Test large-scale Git repositories**  

---

## 🐝 License  
This project is licensed under the **MIT License**.  
Feel free to modify, share, or improve the script!  

