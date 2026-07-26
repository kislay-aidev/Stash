# In the previous version, when using the parameter - target_folder in if block, os.path.exists(target_folder)
# I encountered bug a bug where, after moving the files into their respective folder,
# the skip-line is being printed repeatedly for each file. The skip condition for 'Duplicate Detection'.

# since the target_folder looks like something: C:\Users\kisla\Downloads\Project\Documents\PDFs
# After the first run, the folder exists. Therefore, os.path.exists(target_folder) returns 'True'
# for every PDF.
# So your program says:

# Skipped: Java Lecture 6.pdf already exists.
# Skipped: Welcome Class.pdf already exists.

# even if the file doesn't exist there.

# Intended to check for the 'destintion_path' instead of the 'target_folder' help me, uncover this bug and find the root cause.
# So, changed the condition from - if os.path.exists(target_folder): skip, to - if os.path.exists(destination_folder): skip
# to check if the file is peresnt at the destination folder or not.

# Second bug - Welcome Class.pdf was inside Images folder.

            # Another Welcome Class.pdf was already inside Documents/PDFs.

            # After 're-running' the program, the original one disappeared.

# Found this weird behaviour because of using 'shutil.move' method instead of the 'os.rename' method.
# Since the 'os.rename' method flags an error - if destination already exists.
# shutil.move() is more aggressive.
# Depending on the situation, it can overwrite or replace files.

# For example: Images/Welcome Class.pdf

                # got moved into
# Documents/PDFs/Welcome Class.pdf

                # and replaced the existing file.

                # Result:
# Original PDF lost

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

for current_path, foldernames, filenames in os.walk(project_folder):
    for fl in filenames:
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
