# here, changed the condition of renaming duplicates as: 'file(1).txt', 'file(2).txt', from:
# for nums in range(1, 100):
    # # Add number to filename before extension
    # base, ext = os.path.splitext(destination_path)
    # new_name = f"{base}({nums}){ext}"   # e.g., file(1).txt, file(2).txt, etc.

    # if not os.path.exists(new_name):
        #     shutil.move(source_path, new_name)
        #     break

# To the condition of:
# Split into base + extension
# base, ext = os.path.splitext(os.path.join(target_folder, fl))
# <--- use original fl here, and not destination_path after renaming

# nums = 1

# while True:
#     new_name = f"{base}({nums}){ext}"

#     if not os.path.exists(new_name):
#         shutil.move(source_path, new_name)
#         break

#     nums += 1

# This change of the renaming condition for duplicate files, changed the flow of code 
# and also uplift the artificial limit of numbers (for file renaming)  by the for loop, 
# making moving of duplicte files in large number, to a specific location, possible.



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
        # print(f"CURRENT PATH: {current_path}")
        # print(f"FILE: {fl}")

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
                # print("SOURCE:", source_path)
                # print("DESTINATION:", destination_path)
                # print("DEST EXISTS:", os.path.exists(destination_path))
                # print("----------------")
                if os.path.exists(destination_path):

                    # Split into base + extension
                    base, ext = os.path.splitext(os.path.join(target_folder, fl))
                    # <--- use original fl here, and not destination_path after renaming

                    nums = 1

                    while True:
                        new_name = f"{base}({nums}){ext}"

                        if not os.path.exists(new_name):
                            shutil.move(source_path, new_name)
                            break

                        nums += 1
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

                    # Split into base + extension
                    base, ext = os.path.splitext(os.path.join(target_folder, fl))
                    # <--- use original fl here, and not destination_path after renaming

                    nums = 1

                    while True:
                        new_name = f"{base}({nums}){ext}"

                        if not os.path.exists(new_name):
                            shutil.move(source_path, new_name)
                            break

                        nums += 1
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

                    # Split into base + extension
                    base, ext = os.path.splitext(os.path.join(target_folder, fl))
                    # <--- use original fl here, and not destination_path after renaming

                    nums = 1

                    while True:
                        new_name = f"{base}({nums}){ext}"

                        if not os.path.exists(new_name):
                            shutil.move(source_path, new_name)
                            break

                        nums += 1
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

                    # Split into base + extension
                    base, ext = os.path.splitext(os.path.join(target_folder, fl))
                    # <--- use original fl here, and not destination_path after renaming

                    nums = 1

                    while True:
                        new_name = f"{base}({nums}){ext}"

                        if not os.path.exists(new_name):
                            shutil.move(source_path, new_name)
                            break

                        nums += 1
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

                    # Split into base + extension
                    base, ext = os.path.splitext(os.path.join(target_folder, fl))
                    # <--- use original fl here, and not destination_path after renaming

                    nums = 1

                    while True:
                        new_name = f"{base}({nums}){ext}"

                        if not os.path.exists(new_name):
                            shutil.move(source_path, new_name)
                            break

                        nums += 1
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

                    # Split into base + extension
                    base, ext = os.path.splitext(os.path.join(target_folder, fl))
                    # <--- use original fl here, and not destination_path after renaming

                    nums = 1

                    while True:
                        new_name = f"{base}({nums}){ext}"

                        if not os.path.exists(new_name):
                            shutil.move(source_path, new_name)
                            break

                        nums += 1
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

                    # Split into base + extension
                    base, ext = os.path.splitext(os.path.join(target_folder, fl))
                    # <--- use original fl here, and not destination_path after renaming

                    nums = 1

                    while True:
                        new_name = f"{base}({nums}){ext}"

                        if not os.path.exists(new_name):
                            shutil.move(source_path, new_name)
                            break

                        nums += 1
                else:
                    shutil.move(source_path, destination_path)  # Move the file to the target folder
                    print(f"Moved: '{fl}'")
