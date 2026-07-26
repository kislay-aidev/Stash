# here, added the if os.path.exists(destination) : print skip, else: move the file
# this nuance tells the system that if you found a file, that already exists in the destination folder, one more time
# then skip the moving of that file, and print - skipped, the file already exists
# If the file is a new one and does not exists in the 'destination folder' it gets moved by "shutil.move" method in the else block.
# This small change checks for the file duplicacy, the "Duplicate Detection", and skips moving the file, if it's present there.
# Here, I accidently used the "target_folder" in the if block - os.path.exists(target_folder).


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
                shutil.move(source_path, destination_path)

                if os.path.exists(target_folder):
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
                shutil.move(source_path, destination_path)

                if os.path.exists(target_folder):
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
                shutil.move(source_path, destination_path)

                if os.path.exists(target_folder):
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
                shutil.move(source_path, destination_path)

                if os.path.exists(target_folder):
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
                shutil.move(source_path, destination_path)

                if os.path.exists(target_folder):
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
                shutil.move(source_path, destination_path)

                if os.path.exists(target_folder):
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
                shutil.move(source_path, destination_path)
                
                if os.path.exists(target_folder):
                    print(f"Skipped: '{fl}' already exists.")
                    # print(f"Target folder '{target_folder}' already exists.")
                else:
                    shutil.move(source_path, destination_path)  # Move the file to the target folder
                    print(f"Moved: '{fl}'")
