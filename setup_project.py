import os

folders = [
    "0_data/raw", "0_data/cleaned", "0_data/exports",
    "1_notebooks",
    "2_src",
    "3_reports",
    "4_app",
    "visuals"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create placeholder files
open("README.md", "w").close()
open("requirements.txt", "w").close()
open(".gitignore", "w").close()

print("✅ Folder structure created successfully!")
