import os

# print(os.getcwd())

os.chdir("C:\\Users\\kisla\\Downloads\\Project")

project_folder = os.getcwd()

# print(os.listdir(project_folder))

for current_path, foldernames, filenames in os.walk(project_folder):
    for fl in filenames:
        # print(fl)

# Documents Folders creation        
        if os.path.splitext(fl)[1] == '.pdf' or os.path.splitext(fl)[1] == '.txt' or os.path.splitext(fl)[1] == '.docx' or os.path.splitext(fl)[1] == '.pptx' or os.path.splitext(fl)[1] == '.docs' :
            for name in ["Documents/Word Docs", "Documents/PDFs", "Documents/Presentations", "Documents/Text Files"]:
                if not os.path.exists(name):
                    os.makedirs(name)

# Images Folders creation
        elif os.path.splitext(fl)[1] == '.jpg' or os.path.splitext(fl)[1] == '.jpeg' or os.path.splitext(fl)[1] == '.png':
            for name in ["Images/JPGs", "Images/PNGs"]:
                if not os.path.exists(name):
                    os.makedirs(name)

# Gifs Folder creation
        elif os.path.splitext(fl)[1] == '.gif':
            for name in ["GIFs"]:
                if not os.path.exists(name):
                    os.makedirs(name)

# Videos (Movies) & Subtitles Folders creation
        elif os.path.splitext(fl)[1] == '.mp4' or os.path.splitext(fl)[1] == '.avi' or os.path.splitext(fl)[1] == '.mov' or os.path.splitext(fl)[1] == '.mkv' or os.path.splitext(fl)[1] == '.webm':
            for name in ["Videos/MP4s", "Videos/AVIs", "Videos/MOVs", "Videos/MKVs", "Videos/WEBMs"]:
                if not os.path.exists(name):
                    os.makedirs(name)

        elif os.path.splitext(fl)[1] == '.srt' or os.path.splitext(fl)[1] == '.sub' or os.path.splitext(fl)[1] == '.vtt':
            for name in ["Videos/Subtitles/SRTs", "Videos/Subtitles/SUBs", "Videos/Subtitles/VTTs"]:
                if not os.path.exists(name):
                    os.makedirs(name)

# Music & Lyrics Folders creation
        elif os.path.splitext(fl)[1] == '.mp3' or os.path.splitext(fl)[1] == '.wav' or os.path.splitext(fl)[1] == '.flac' or os.path.splitext(fl)[1] == '.opus' or os.path.splitext(fl)[1] == '.aac' or os.path.splitext(fl)[1] == '.m4a':
            for name in ["Music/MP3s", "Music/WAVs", "Music/FLACs", "Music/OPUSs", "Music/AACs", "Music/M4As"]:
                if not os.path.exists(name):
                    os.makedirs(name)

        elif os.path.splitext(fl)[1] == '.lrc':
            for name in ["Music/LRCs"]:
                if not os.path.exists(name):
                    os.makedirs(name)

# Archives Folders creation
        elif os.path.splitext(fl)[1] == '.zip' or os.path.splitext(fl)[1] == '.rar' or os.path.splitext(fl)[1] == '.7z' or os.path.splitext(fl)[1] == '.tar' or os.path.splitext(fl)[1] == '.gz':
            for name in ["Archives/ZIPs", "Archives/RARs", "Archives/7Zs", "Archives/TARs", "Archives/GZs"]:
                if not os.path.exists(name):
                    os.makedirs(name)

        else:
            for name in ["Others"]:
                if not os.path.exists(name):
                    os.makedirs(name)
