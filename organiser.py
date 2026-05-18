import os
import shutil

# Asking user to enter folder path
folder_path = input("Enter the folder path: ")

# Checking whether folder exists or not
if not os.path.exists(folder_path):
    print("Folder does not exist.")
    exit()

# File categories
image_extensions = [".jpg", ".jpeg", ".png", ".gif"]
document_extensions = [".pdf", ".docx", ".txt"]
video_extensions = [".mp4", ".mkv", ".avi"]

# Getting all files from folder
files = os.listdir(folder_path)

# Loop through each file
for file in files:

    # Full file path
    file_location = os.path.join(folder_path, file)

    # Skip folders
    if os.path.isdir(file_location):
        continue

    # Extract file extension
    file_name, extension = os.path.splitext(file)

    # Decide destination folder
    if extension.lower() in image_extensions:
        destination_folder = "Images"

    elif extension.lower() in document_extensions:
        destination_folder = "Docs"

    elif extension.lower() in video_extensions:
        destination_folder = "Videos"

    else:
        destination_folder = "Others"

    # Create folder if it doesn't exist
    new_folder_path = os.path.join(folder_path, destination_folder)

    if not os.path.exists(new_folder_path):
        os.mkdir(new_folder_path)

    # Move file into folder
    shutil.move(file_location, os.path.join(new_folder_path, file))

    print(file, "moved to", destination_folder)

print("All files organized successfully.")