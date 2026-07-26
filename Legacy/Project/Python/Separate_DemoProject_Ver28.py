# change 1 - Right now 'Statistics.json' file only stores the latest run’s stats (a single dictionary).
# If want to preserve a history of runs, 
# store a list of dictionaries, appending a new record each time the program executes.

# Current behavior: 
# {
#   "Run Time": "2026-06-24 02:35:20",
#   "Files Processed": 12,
#   "Files Moved": 10,
#   "Duplicate Files Renamed": 2,
#   "Unknown Files Found": 0
# }
# Each run overwrites the file.

# Desired behavior:
# [
#   {
#     "Run Time": "2026-06-24 02:35:20",
#     "Files Processed": 12,
#     "Files Moved": 10,
#     "Duplicate Files Renamed": 2,
#     "Unknown Files Found": 0
#   },
#   {
#     "Run Time": "2026-06-24 02:40:05",
#     "Files Processed": 8,
#     "Files Moved": 7,
#     "Duplicate Files Renamed": 1,
#     "Unknown Files Found": 0
#   }
# ]
# Now every execution is preserved.

import os
import shutil
import json
from datetime import datetime

os.chdir(r"C:\Users\kisla\Desktop\FileOrgProject")

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
    # ".json": "WebPages/JSON",

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
    # ".log": "Others/Logs",
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

# Making ".system" folder to contain all the logs file and the "statistic.json" file

# Making "logs" folder inside ".system" folder
os.makedirs(".system/logs", exist_ok=True)

# Making "stats" folder inside ".system" folder
os.makedirs(".system/stats", exist_ok=True)

# linking or joining the paths of ".system/logs" folder with the ".log" files
log_file = os.path.join(
    ".system/logs",
    datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S.log"
    )
)

# linking or joining the paths of ".system/stats" folder with the "Statistics.json" files
stats_file = os.path.join(
    ".system/stats",
    "Statistics.json"
)

# writing the BASE 'Statistics.json' script:
files_processed = 0
files_moved = 0
duplicates_renamed = 0
unknown_files = 0

stats_file = ".system/stats/Statistics.json"

# Prepare current run stats
stats = {
    "Run Time" : datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    ),
    "Files Processed": files_processed,
    "Files Moved": files_moved,
    "Duplicate Files Renamed": duplicates_renamed,
    "Unknown Files Found": unknown_files
}

# # Load existing history if file exists
# if os.path.exists(stats_file):
#     with open(stats_file, "r") as f:
#         try:
#             history = json.load(f)
#         except json.JSONDecodeError:
#             history = []
# else:
#     history = []

# Load existing history safely
if os.path.exists(stats_file):
    try:
        with open(stats_file, "r") as f:
            history = json.load(f)
            # Ensure it's a list
            if not isinstance(history, list):
                history = []
    except (json.JSONDecodeError, FileNotFoundError):
        history = []
else:
    history = []

# Append current run
history.append(stats)

# Save back
with open(stats_file, "w") as f:
    json.dump(history, f, indent=2)

print("Stats appended to Statistics.json")

# Function for safe moving of duplicate files by renaming them, and then moving the file
def safe_move(source_path, destination_path):

    """Move file safely, handling duplicates."""
    log_message = ""

# Getting the File Name and the Source folder, in which it is currently sitting before its movement.
    source_name = os.path.basename(source_path)

    source_folder = os.path.basename(
        os.path.dirname(source_path)
    )

# Getting the destination Folder for keeping the file movement record
    relative_destination = os.path.relpath(
        destination_path,
        project_folder
    )

    destination_folder = os.path.basename(
        os.path.dirname(relative_destination)
    )
    
    # Split into base (file name) + extension
    base, ext = os.path.splitext(destination_path)

    if os.path.exists(destination_path):
        # DUPLICATE HANDLING

        # File already exists → rename duplicate
        # logic to rename file here...

        nums = 1
        while True:
            # Naming duplicates as:
            # file(1).txt
            # file(2).txt

            new_name = f"{base}({nums}){ext}"

            # Moving of Duplicate files into the same folder where the "Original File" resides.
            if not os.path.exists(new_name):
                shutil.move(source_path, new_name)

                stats["Duplicate Files Renamed"] += 1 # increment AFTER successful rename

                stats["Files Moved"] += 1 # increment after successfull moving of duplicate file after renaming.

                stats["Files Processed"] += 1 # for total files processed, whether moved or not.

                print(f"Moved duplicate as: {new_name}")

                # Duplicate file logging
                log_message = (
                    f"Duplicate renamed: "
                    f"{source_name} -> {os.path.basename(new_name)} "
                    f"from {source_folder} "
                    f"to {destination_folder}"
                )

                break
            nums += 1
    else:
        shutil.move(source_path, destination_path)

        # managing moved 'FILES' stats
        stats["Files Moved"] += 1 # increment after successfull moving of duplicate file after renaming.

        stats["Files Processed"] += 1 # for total files processed, whether moved or not.

        print(f"Moved: {destination_path}")
        
        log_message = (
            f"Moved: {source_name} "
            f"from {source_folder} "
            f"to {destination_folder}"
        )

# Logging entries of file movement with inclusion of timestamps in the "log" file.

    with open(log_file, "a") as log:
            timestamp = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            log.write(
                f"[{timestamp}] {log_message}\n"
            )

for current_path, foldernames, filenames in os.walk(project_folder):
    # Skip already-organized folders
    foldernames[:] = [
        f for f in foldernames
        if f not in ["Documents","Images","Videos","Music","Archives",
                     "Project","WebPages","Others","GIFs", ".system"]
    ]

    for fl in filenames:
        extension = os.path.splitext(fl)[1].lower()
        source_path = os.path.join(current_path, fl)

        if extension in all_extensions:
            # normal MOVE LOGIC
            target_folder = os.path.join(project_folder, all_extensions[extension])
        else:
            target_folder = os.path.join(project_folder, "Others/Unknown")

            # Count files with extensions not present in the mapping
            stats["Unknown Files Found"] += 1
            # move to Others/Unknown folder

        os.makedirs(target_folder, exist_ok=True)
        destination_path = os.path.join(target_folder, fl)

        if source_path != destination_path and os.path.exists(source_path):

            if extension not in all_extensions:
                stats["Unknown Files Found"] += 1   # increment only when actually moving
            
            safe_move(source_path, destination_path)


# creating 'Statistics.json' file with already prepared BASE script and other data.
with open (stats_file, "w") as f:
    json.dump(stats, f, indent=2)

print("Stats written to Statistics.json")