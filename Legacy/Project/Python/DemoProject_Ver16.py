# The codefile was very repetitive.
# most of the work was under repeitive loop.
# Like: making of folders, moving of files, 
# checking of duplicates, moving of duplucate files and renaming it while moving.
# All of it was done with using loops and conditional statements.

# For each type of the folder, whether Documents, Images, Videos, GIFs, etc 
# required separate for-if-for-if nested block to do the above said tasks.
# It made the work done with correct logic and no errors, but came with a cost of repetitive code structure.
# By which, the code maintainance became tedious.

# To reduce the code redundancy, 
# introduced clubbing all the extension maps into: "all_extension" dict.
# Now, the 'all_extension' dict. is being used to manage all the extension-folder mapping.
# Moreover, build/grouped the entire logic of handling files safely and checking duplicates,
# inside a "def safe_move" function. Which helps with the duplicate files problem.
# next, added a universal logic (applied to this File Organizer script only) where, the rest of the work is done.
# From making of folders, to moving of files, to traversing of folders, all inside single fore-if-for block.

# Now, it reduced the redundancy, made the code more maintanable.
# And also, the codespace is now more efficient.


import os
import shutil

os.chdir("C:\\Users\\kisla\\Downloads\\Project")

project_folder = os.getcwd()

# Define mapping of 'Document'extensions to folders
doc_ext_map = {
    ".pdf": "Documents/PDFs",
    ".txt": "Documents/Text Files",
    ".docx": "Documents/Word Docs",
    ".doc": "Documents/Word Docs",
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
    ".json": "WebPages/JSON",

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
    ".ai": "Images/Illustrator",

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

# --- Merge all maps into one ---
all_extensions = {}
all_extensions.update(doc_ext_map)
all_extensions.update(img_ext_map)
all_extensions.update(gif_ext_map)
all_extensions.update(videoSub_ext_map)
all_extensions.update(musicLrc_ext_map)
all_extensions.update(archive_ext_map)
all_extensions.update(other_ext_map)

def safe_move(source_path, destination_path):
    """Move file safely, handling duplicates."""
    
    # Split into base + extension
    base, ext = os.path.splitext(destination_path)

    if os.path.exists(destination_path):
        nums = 1
        while True:

            """Naming of Duplicate files as: file(1).txt, file(2).txt, etc."""
            new_name = f"{base}({nums}){ext}"

            #Moving of Duplicate files into the same folder where the "Original File" resides.
            if not os.path.exists(new_name):
                shutil.move(source_path, new_name)
                print(f"Moved duplicate as: {new_name}")
                break
            nums += 1
    else:
        shutil.move(source_path, destination_path)
        print(f"Moved: {destination_path}")

for current_path, foldernames, filenames in os.walk(project_folder):
    # Skip already-organized folders
    foldernames[:] = [
        f for f in foldernames
        if f not in ["Documents","Images","Videos","Music","Archives",
                     "Project","WebPages","Others","GIFs"]
    ]

    for fl in filenames:
        extension = os.path.splitext(fl)[1].lower()
        source_path = os.path.join(current_path, fl)

        if extension in all_extensions:
            target_folder = os.path.join(project_folder, all_extensions[extension])
        else:
            target_folder = os.path.join(project_folder, "Others/Unknown")

        os.makedirs(target_folder, exist_ok=True)
        destination_path = os.path.join(target_folder, fl)

        if source_path != destination_path and os.path.exists(source_path):
            safe_move(source_path, destination_path)
