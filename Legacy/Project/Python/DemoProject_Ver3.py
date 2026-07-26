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
        if extension == '.pdf' or extension == '.txt' or extension == '.docx' or extension == '.pptx' or extension == '.docs' :
            for name in ["Documents/Word Docs", "Documents/PDFs", "Documents/Presentations", "Documents/Text Files"]:
                if not os.path.exists(name):
                    os.makedirs(name)

# Images Folders creation
        elif extension == '.jpg' or extension == '.jpeg' or extension == '.png':
            for name in ["Images/JPGs", "Images/PNGs"]:
                if not os.path.exists(name):
                    os.makedirs(name)

# Gifs Folder creation
        elif extension == '.gif':
            for name in ["GIFs"]:
                if not os.path.exists(name):
                    os.makedirs(name)

# Videos (Movies) & Subtitles Folders creation
        elif extension == '.mp4' or extension == '.avi' or extension == '.mov' or extension == '.mkv' or extension == '.webm':
            for name in ["Videos/MP4s", "Videos/AVIs", "Videos/MOVs", "Videos/MKVs", "Videos/WEBMs"]:
                if not os.path.exists(name):
                    os.makedirs(name)

        elif extension == '.srt' or extension == '.sub' or extension == '.vtt':
            for name in ["Videos/Subtitles/SRTs", "Videos/Subtitles/SUBs", "Videos/Subtitles/VTTs"]:
                if not os.path.exists(name):
                    os.makedirs(name)

# Music & Lyrics Folders creation
        elif extension == '.mp3' or extension == '.wav' or extension == '.flac' or extension == '.opus' or extension == '.aac' or extension == '.m4a':
            for name in ["Music/MP3s", "Music/WAVs", "Music/FLACs", "Music/OPUSs", "Music/AACs", "Music/M4As"]:
                if not os.path.exists(name):
                    os.makedirs(name)

        elif extension == '.lrc':
            for name in ["Music/LRCs"]:
                if not os.path.exists(name):
                    os.makedirs(name)

# Archives Folders creation
        elif extension == '.zip' or extension == '.rar' or extension == '.7z' or extension == '.tar' or extension == '.gz':
            for name in ["Archives/ZIPs", "Archives/RARs", "Archives/7Zs", "Archives/TARs", "Archives/GZs"]:
                if not os.path.exists(name):
                    os.makedirs(name)

        else:
            for name in ["Others"]:
                if not os.path.exists(name):
                    os.makedirs(name)
