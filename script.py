import os
import json
import requests
import base64
import time

CONFIG_FILE = "config.json"

# Function to load or create config.json
def load_or_create_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            config = json.load(file)
        return config
    else:
        print("🔑 First-time setup: Enter your GitHub details")
        github_api_key = input("Enter your GitHub API Key: ").strip()
        github_username = input("Enter your GitHub Username: ").strip()
        repo_name = input("Enter your Repository Name: ").strip()

        config = {
            "GITHUB_API_KEY": github_api_key,
            "REPO_OWNER": github_username,
            "REPO_NAME": repo_name
        }

        with open(CONFIG_FILE, "w") as file:
            json.dump(config, file, indent=4)

        print("✅ Configuration saved! Running script...")
        return config

# Load the config
config = load_or_create_config()

# GitHub API Credentials
GITHUB_API_KEY = config["GITHUB_API_KEY"]
REPO_OWNER = config["REPO_OWNER"]
REPO_NAME = config["REPO_NAME"]

# GitHub API Headers
HEADERS = {
    "Authorization": f"token {GITHUB_API_KEY}",
    "Accept": "application/vnd.github.v3+json"
}

# Function to create a file in GitHub repository
def create_file(file_path, content):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{file_path}"
    data = {
        "message": f"Create {file_path}",
        "content": base64.b64encode(content.encode("utf-8")).decode("utf-8")
    }
    response = requests.put(url, headers=HEADERS, json=data)
    
    if response.status_code == 201:
        print(f"✅ Created: {file_path}")
    else:
        print(f"❌ Failed to create {file_path}: {response.json()}")

# Function to create a folder with 1,000 files
def create_folder_with_files(folder_number):
    folder_name = f"folder_{folder_number}"
    print(f"📁 Creating {folder_name} with 1000 files...")

    for file_num in range(1, 1001):  # Create 1,000 files per folder
        file_path = f"{folder_name}/file_{file_num}.txt"
        content = f"This is file {file_num} in {folder_name}"
        create_file(file_path, content)

# Infinite loop to create unlimited folders
def main():
    folder_counter = 1
    while True:
        create_folder_with_files(folder_counter)
        folder_counter += 1  # Increment folder count
        time.sleep(1)  # Short delay to avoid rate limit issues

if __name__ == "__main__":
    main()
      
