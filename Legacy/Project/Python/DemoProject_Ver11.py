# So, added: 
# print(f"CURRENT PATH: {current_path}")
# print(f"FILE: {fl}")
# Immediately after:
# for fl in filenames:

# Also added:
# print("SOURCE:", source_path)
# print("DESTINATION:", destination_path)
# print("DEST EXISTS:", os.path.exists(destination_path))
# print("----------------")
# Right before:
# if os.path.exists(destination_path):

# After adding these test cases for testing os.walk() behaviour for the bug, result was:

# CURRENT PATH: C:\Users\kisla\Downloads\Project\Documents\PDFs
# FILE: Java Lecture 1.pdf
# Skipped: 'Java Lecture 1.pdf' already exists.

# CURRENT PATH: C:\Users\kisla\Downloads\Project\Documents\PDFs
# FILE: Java Lecture 2.pdf
# Skipped: 'Java Lecture 2.pdf' already exists.

# program is not checking duplicates in the original folder.

# It is literally entering:

# Project
# └── Documents
#     └── PDFs

# and then finding:

# Java Lecture 1.pdf
# Java Lecture 2.pdf
# Java Lecture 3.pdf
# ...

# which are already sitting there.

# Then it computes:

# source_path =
# C:\Users\kisla\Downloads\Project\Documents\PDFs\Java Lecture 1.pdf

# destination_path =
# C:\Users\kisla\Downloads\Project\Documents\PDFs\Java Lecture 1.pdf

# which means:

# source_path == destination_path

# Same file.

# Same location.

# No move needed.

# But because the file exists:

# os.path.exists(destination_path)

# returns:

# True

# therefore:

# Skipped: 'Java Lecture 1.pdf' already exists.

# gets printed.

# Actual Problem: "organizer is organizing its own organized folders."

# SOLUTION:
# added:
# foldernames[:] = [
#     folder
#     for folder in foldernames
#     if folder not in [
#         "Documents",
#         "Images",
#         "Videos",
#         "Music",
#         "Archives",
#         "GIFs",
#         "Others"
#     ]
# ] 

# OR

# foldernames[:] = [
#     f for f in foldernames
#     if f not in ["Documents", "Images", "Videos", "Music", "Archives"]
# ]

# Immediately after:
# for current_path, foldernames, filenames in os.walk(project_folder):

#This modifies the traversal list.

# Now os.walk will NOT enter:

# Documents/
# Images/
# Videos/
# Music/
# Archives/
# GIFs/
# Others/

# at all.

# This is a classic bug:

# Recursive self-processing

# The program creates folders and then processes those folders on the next scan.

import os
import shutil

os.chdir("C:\\Users\\kisla\\Downloads\\Project")

project_folder = os.getcwd()

# Define mapping of 'Document'extensions to folders
doc_ext_map = {
    ".pdf": "Documents/PDFs",
    ".txt": "Documents/Text Files",
    ".docx": "Documents/Word Docs",
    ".docs": "Documents/Word Docs",
    ".pptx": "Documents/Presentations",
    ".xlsx": "Documents/Spreadsheets",
    ".csv": "Documents/CSV Files",
}

# Define mapping of 'Image' extensions to folders
img_ext_map = {
    ".jpg": "Images/JPGs",
    ".jpeg": "Images/JPEGs",
    ".png": "Images/PNGs"
}

# Define mapping of 'Gif' extensions to folders
gif_ext_map = {
    ".gif": "GIFs"
}

# Define mapping of 'Video & Subtitles' extensions to folders
videoSub_ext_map = {
    ".mp4": "Videos/MP4s",
    ".avi": "Videos/AVIs",
    ".mov": "Videos/MOVs",
    ".mkv": "Videos/MKVs",
    ".webm": "Videos/WEBMs",
    ".srt": "Videos/Subtitles/SRTs",
    ".sub": "Videos/Subtitles/SUBs",
    ".vtt": "Videos/Subtitles/VTTs"
}

# Define mapping of 'Music & Lyrics' extensions to folders
musicLrc_ext_map = {
    ".mp3": "Music/MP3s",
    ".wav": "Music/WAVs",
    ".flac": "Music/FLACs",
    ".opus": "Music/OPUSs",
    ".aac": "Music/AACs",
    ".m4a": "Music/M4As",
    ".lrc": "Music/LRCs"
}

# Define mapping of 'Archives' extensions to folders
archive_ext_map = {
    ".zip": "Archives/ZIPs",
    ".rar": "Archives/RARs",
    ".7z": "Archives/7Zs",
    ".tar": "Archives/TARs",
    ".gz": "Archives/GZs"
}

# Define mapping of Other extensions to folders
other_ext_map = {
    # Code / Notebooks
    ".py": "Project/Python",
    ".ipynb": "Project/Notebooks",
    ".sh": "Project/Scripts",
    ".ps1": "Project/Scripts",

    # Web / frontend
    ".html": "WebPages",
    ".htm": "WebPages",
    ".css": "WebPages/CSS",
    ".js": "WebPages/JS",
    ".mjs": "WebPages/JS",
    ".ts": "WebPages/TS",
    ".jsx": "WebPages/JSX",
    ".tsx": "WebPages/TSX",
    ".json": "Webpages/JSON",

    # Markup / docs
    ".md": "Documents/Text Files",
    ".rst": "Documents/Text Files",
    ".tex": "Documents/Text Files",
    ".epub": "Documents/EPUBs",

    # Config / data
    ".xml": "Others/XML",
    ".yml": "Others/YAML",
    ".yaml": "Others/YAML",
    ".ini": "Others/Configs",
    ".cfg": "Others/Configs",
    ".log": "Others/Logs",
    ".sql": "Others/SQL",
    ".db": "Others/Databases",
    ".sqlite": "Others/Databases",

    # Images / vector / design
    ".svg": "Images/SVGs",
    ".psd": "Images/PSD",
    ".ai": "Images/AI",

    # Binaries / installers / archives (some already covered)
    ".exe": "Others/Executables",
    ".msi": "Others/Executables",
    ".apk": "Others/APKs",
    ".bin": "Others/Binaries",
    ".dll": "Others/Binaries",
    ".iso": "Others/ISOs",

    # Misc / contacts / calendar / torrents
    ".vcf": "Others/Contacts",
    ".ics": "Others/Calendars",
    ".torrent": "Others/Torrents",
    ".bak": "Others/Backups"
}

for current_path, foldernames, filenames in os.walk(project_folder):
    for fl in filenames:
        print(f"CURRENT PATH: {current_path}")
        print(f"FILE: {fl}")

        # extension separation/segregation
        extension = os.path.splitext(fl)[1].lower() # Gets the file extension and converts it to lowercase for uniformity.

# Documents Folders creation        
        if extension in doc_ext_map:
            target_folder = os.path.join(project_folder, doc_ext_map[extension])

            os.makedirs(target_folder, exist_ok=True)  # Create the target folder if it doesn't exist

            #source and destination paths for moving the file
            source_path = os.path.join(current_path, fl)
            destination_path = os.path.join(target_folder, fl)

            # move the file to the target folder only if exits and is not already in the target folder.
            if os.path.exists(source_path) and source_path != destination_path:
                print("SOURCE:", source_path)
                print("DESTINATION:", destination_path)
                print("DEST EXISTS:", os.path.exists(destination_path))
                print("----------------")
                if os.path.exists(destination_path):
                    print(f"Skipped: '{fl}' already exists.")
                    # print(f"Target folder '{target_folder}' already exists.")
                else:
                    shutil.move(source_path, destination_path)  # Move the file to the target folder
                    print(f"Moved: '{fl}'")

# Images Folders creation
        elif extension in img_ext_map:
            target_folder = os.path.join(project_folder, doc_ext_map[extension])

            os.makedirs(target_folder, exist_ok=True)  # Create the target folder if it doesn't exist

            #source and destination paths for moving the file
            source_path = os.path.join(current_path, fl)
            destination_path = os.path.join(target_folder, fl)

            # move the file to the target folder only if exits and is not already in the target folder.
            if os.path.exists(source_path) and source_path != destination_path:
                if os.path.exists(destination_path):
                    print(f"Skipped: '{fl}' already exists.")
                    # print(f"Target folder '{target_folder}' already exists.")
                else:
                    shutil.move(source_path, destination_path)  # Move the file to the target folder
                    print(f"Moved: '{fl}'")
           
# Gifs Folder creation
        elif extension in gif_ext_map:
            target_folder = os.path.join(project_folder, doc_ext_map[extension])

            os.makedirs(target_folder, exist_ok=True)  # Create the target folder if it doesn't exist

            #source and destination paths for moving the file
            source_path = os.path.join(current_path, fl)
            destination_path = os.path.join(target_folder, fl)

            # move the file to the target folder only if exits and is not already in the target folder.
            if os.path.exists(source_path) and source_path != destination_path:
                if os.path.exists(destination_path):
                    print(f"Skipped: '{fl}' already exists.")
                    # print(f"Target folder '{target_folder}' already exists.")
                else:
                    shutil.move(source_path, destination_path)  # Move the file to the target folder
                    print(f"Moved: '{fl}'")

# Videos (Movies) & Subtitles Folders creation
        elif extension in videoSub_ext_map:
            target_folder = os.path.join(project_folder, doc_ext_map[extension])

            os.makedirs(target_folder, exist_ok=True)  # Create the target folder if it doesn't exist

            #source and destination paths for moving the file
            source_path = os.path.join(current_path, fl)
            destination_path = os.path.join(target_folder, fl)

            # move the file to the target folder only if exits and is not already in the target folder.
            if os.path.exists(source_path) and source_path != destination_path:
                if os.path.exists(destination_path):
                    print(f"Skipped: '{fl}' already exists.")
                    # print(f"Target folder '{target_folder}' already exists.")
                else:
                    shutil.move(source_path, destination_path)  # Move the file to the target folder
                    print(f"Moved: '{fl}'")

        # elif extension in ['.srt', '.sub', '.vtt']:
        #     for name in ["Videos/Subtitles/SRTs", "Videos/Subtitles/SUBs", "Videos/Subtitles/VTTs"]:
        #         if not os.path.exists(name):
        #             os.makedirs(name)

# Music & Lyrics Folders creation
        elif extension in musicLrc_ext_map:
            target_folder = os.path.join(project_folder, doc_ext_map[extension])

            os.makedirs(target_folder, exist_ok=True)  # Create the target folder if it doesn't exist

            #source and destination paths for moving the file
            source_path = os.path.join(current_path, fl)
            destination_path = os.path.join(target_folder, fl)

            # move the file to the target folder only if exits and is not already in the target folder.
            if os.path.exists(source_path) and source_path != destination_path:
                if os.path.exists(destination_path):
                    print(f"Skipped: '{fl}' already exists.")
                    # print(f"Target folder '{target_folder}' already exists.")
                else:
                    shutil.move(source_path, destination_path)  # Move the file to the target folder
                    print(f"Moved: '{fl}'")

        # elif extension in ['.lrc']:
        #     for name in ["Music/LRCs"]:
        #         if not os.path.exists(name):
        #             os.makedirs(name)

# Archives Folders creation
        elif extension in archive_ext_map:
            target_folder = os.path.join(project_folder, doc_ext_map[extension])

            os.makedirs(target_folder, exist_ok=True)  # Create the target folder if it doesn't exist

            #source and destination paths for moving the file
            source_path = os.path.join(current_path, fl)
            destination_path = os.path.join(target_folder, fl)

            # move the file to the target folder only if exits and is not already in the target folder.
            if os.path.exists(source_path) and source_path != destination_path:
                if os.path.exists(destination_path):
                    print(f"Skipped: '{fl}' already exists.")
                    # print(f"Target folder '{target_folder}' already exists.")
                else:
                    shutil.move(source_path, destination_path)  # Move the file to the target folder
                    print(f"Moved: '{fl}'")

        else:
            target_folder = os.path.join(project_folder, doc_ext_map[extension])

            os.makedirs(target_folder, exist_ok=True)  # Create the target folder if it doesn't exist

            #source and destination paths for moving the file
            source_path = os.path.join(current_path, fl)
            destination_path = os.path.join(target_folder, fl)

            # move the file to the target folder only if exits and is not already in the target folder.
            if os.path.exists(source_path) and source_path != destination_path:
                if os.path.exists(destination_path):
                    print(f"Skipped: '{fl}' already exists.")
                    # print(f"Target folder '{target_folder}' already exists.")
                else:
                    shutil.move(source_path, destination_path)  # Move the file to the target folder
                    print(f"Moved: '{fl}'")
