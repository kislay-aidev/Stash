# To solve the previous problem of "os.rename()" method behaving weirdly and moving the file in every folder (type mismatch) 
# throwing error: FileNotFound
# To solve this, mappped extensions to their specific target folder, instead of looping through all four every time
# created an extension map (a dictionary) where, the keys were the "extensions" mapped with their correct folder structures "Documents/Folder" as pairs.
# for example: ".pdf" key mapped with "Documents/PDFs" folder, ".txt" key mapped with "Documents/Text Files" Folder, etc.
# It solved/had:
# Use a dictionary (ext_map) to map extensions to the correct folder.
# Create only the folder you actually need for that file.
# Move the file once, not four times.


import os

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

for current_path, foldernames, filenames in os.walk(project_folder):
    for fl in filenames:
        # extension separation/segregation
        extension = os.path.splitext(fl)[1].lower() # Gets the file extension and converts it to lowercase for uniformity.

# Documents Folders creation        
        if extension in doc_ext_map:
            for name in [doc_ext_map[extension]]:
                if not os.path.exists(name):
                    os.makedirs(name)
                    os.rename(
                        os.path.join(current_path, fl),
                        os.path.join(name, fl)
                    )

# Images Folders creation
        elif extension in ['.jpg', '.jpeg', '.png']:
            for name in ["Images/JPGs", "Images/PNGs"]:
                if not os.path.exists(name):
                    os.makedirs(name)
                    os.rename(
                        os.path.join(current_path, fl),
                        os.path.join(name, fl)
                    )

# Gifs Folder creation
        elif extension in ['.gif']:
            for name in ["GIFs"]:
                if not os.path.exists(name):
                    os.makedirs(name)
                    os.rename(
                        os.path.join(current_path, fl),
                        os.path.join(name, fl)
                    )

# Videos (Movies) & Subtitles Folders creation
        elif extension in ['.mp4', '.avi', '.mov', '.mkv', '.webm']:
            for name in ["Videos/MP4s", "Videos/AVIs", "Videos/MOVs", "Videos/MKVs", "Videos/WEBMs"]:
                if not os.path.exists(name):
                    os.makedirs(name)

        elif extension in ['.srt', '.sub', '.vtt']:
            for name in ["Videos/Subtitles/SRTs", "Videos/Subtitles/SUBs", "Videos/Subtitles/VTTs"]:
                if not os.path.exists(name):
                    os.makedirs(name)

# Music & Lyrics Folders creation
        elif extension in ['.mp3', '.wav', '.flac', '.opus', '.aac', '.m4a']:
            for name in ["Music/MP3s", "Music/WAVs", "Music/FLACs", "Music/OPUSs", "Music/AACs", "Music/M4As"]:
                if not os.path.exists(name):
                    os.makedirs(name)

        elif extension in ['.lrc']:
            for name in ["Music/LRCs"]:
                if not os.path.exists(name):
                    os.makedirs(name)

# Archives Folders creation
        elif extension in ['.zip', '.rar', '.7z', '.tar', '.gz']:
            for name in ["Archives/ZIPs", "Archives/RARs", "Archives/7Zs", "Archives/TARs", "Archives/GZs"]:
                if not os.path.exists(name):
                    os.makedirs(name)

        else:
            for name in ["Others"]:
                if not os.path.exists(name):
                    os.makedirs(name)
