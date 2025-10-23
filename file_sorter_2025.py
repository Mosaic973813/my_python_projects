#!/usr/bin/env python3

import os
import shutil
from pathlib import Path


#Ask for folder name creation
source_folder = input("Please enter the file path of the folder you would like to organize: ")
user_folder_names = input("Please enter preferred folder names seperated by commas: ")
user_folder_names = [name.strip() for name in user_folder_names.split(",") if name.strip()]
default_names = ["Images", "Documents", "Audio", "Videos", "Misc"]

destination_folders = []

#This will allow the python script to find the desktop no matter the OS
desktop = Path.home() / "Desktop"
desktop = desktop if desktop.exists() else Path.home()

#This will add the folder path to the destination folder list
if user_folder_names:
    for folder in user_folder_names:
        name = desktop.joinpath(folder)
        destination_folders.append(name)
else:
    for folder in default_names:
        name = desktop.joinpath(folder)
        destination_folders.append(name)

#This section shows the different files and defines the file paths
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".heic"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".flac"]
}

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

#ChatGpt helped with the below sections

# Validate source folder once before looping
if not os.path.isdir(source_folder):
    print("Invalid folder path. Please check and try again.")
    exit()

# Loop through files in the source folder
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Extract and normalize file extension (includes the '.')
    file_extension = os.path.splitext(filename)[1].lower()

    # Default category if no match found
    matched_category = "Misc"

    # Find which category the file belongs to
    for category, extensions in file_categories.items():
        if file_extension in extensions:
            matched_category = category
            break  # Stop after the first match

    # Build destination path
    destination_folder = desktop / matched_category

    # Create destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Move the file
    shutil.move(file_path, destination_folder)



