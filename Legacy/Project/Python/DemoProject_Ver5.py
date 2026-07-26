# Tested the feature of moving of files into their respective folders with the help of:
# os.rename() method where, I joined the path - current_path, fl to get the source path, and
# name, fl to get the destination path to move those files.
# This was done only with the Documents Folders, and it's files to get the idea ofhow it will work.
# This eventually lead to an error: FileNotFound, which arised when:
# loop runs through every file in the project folder. For each file, the os.walk() method loops to all 4 folder types - PDFs, Word Docs, Presentations, Text Files
# It creates the folders if that doesn't exists and try to os.rename(), that is, move the file, even it the file type is mismatched.
# Example: a '.pdf' file will be moved into Word Docs, then into PDFs, then into Presentations, then into Text Files — 
# until it eventually disappears or throws a FileNotFoundError
# If the folder doesn’t exist yet, os.makedirs(name) works fine, but the rename fails if the file was already moved in a previous iteration.


import os

# print(os.getcwd())

os.chdir("C:\\Users\\kisla\\Downloads\\Project")

project_folder = os.getcwd()

# print(os.listdir(project_folder))

for current_path, foldernames, filenames in os.walk(project_folder):
    for fl in filenames:
        # extension separation/segregation
        extension = os.path.splitext(fl)[1].lower() # Gets the file extension and converts it to lowercase for uniformity.

# Documents Folders creation        
        if extension in ['.pdf', '.txt', '.docx', '.pptx', '.docs']:
            for name in ["Documents/Word Docs", "Documents/PDFs", "Documents/Presentations", "Documents/Text Files"]:
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

# Gifs Folder creation
        elif extension in ['.gif']:
            for name in ["GIFs"]:
                if not os.path.exists(name):
                    os.makedirs(name)

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
