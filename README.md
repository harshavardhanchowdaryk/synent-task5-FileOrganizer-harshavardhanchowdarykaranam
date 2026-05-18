# File Organizer

This project is a simple File Organizer created using Python.

The main purpose of this project is to organize files automatically into separate folders based on their file types.

## Features
- Organizes image files
- Organizes document files
- Organizes video files
- Creates folders automatically
- Moves files into the correct folders

## Modules Used
- os
- shutil

## Technologies Used
- Python
- VS Code

## How the Project Works
1. The user enters the folder path.
2. The program reads all files in that folder.
3. It checks the extension of each file.
4. Files are separated into folders like Images, Docs, Videos, and Others.
5. If the folders are not available, the program creates them automatically.

## Example
Before organizing:
- photo.jpg
- notes.txt
- movie.mp4

After organizing:
- Images/photo.jpg
- Docs/notes.txt
- Videos/movie.mp4

## Output
The folder becomes clean and properly organized automatically.