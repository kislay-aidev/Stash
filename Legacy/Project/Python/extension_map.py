"""
Stash — Extension to folder mappings.

All file extension mappings are centralized here.
Each extension maps to a target subfolder path relative to the project root.
"""

from typing import Dict

# Document extensions
DOC_EXT_MAP: Dict[str, str] = {
    ".pdf": "Documents/PDFs",
    ".txt": "Documents/Text Files",
    ".docx": "Documents/Word Docs",
    ".doc": "Documents/Word Docs",
    ".pptx": "Documents/Presentations",
    ".xlsx": "Documents/Spreadsheets",
    ".csv": "Documents/CSV Files",
}

# Image extensions
IMG_EXT_MAP: Dict[str, str] = {
    ".jpg": "Images/JPGs",
    ".jpeg": "Images/JPEGs",
    ".png": "Images/PNGs",
}

# GIF extensions
GIF_EXT_MAP: Dict[str, str] = {
    ".gif": "GIFs",
}

# Video & Subtitles extensions
VIDEO_EXT_MAP: Dict[str, str] = {
    ".mp4": "Videos/MP4s",
    ".avi": "Videos/AVIs",
    ".mov": "Videos/MOVs",
    ".mkv": "Videos/MKVs",
    ".webm": "Videos/WEBMs",
    ".srt": "Videos/Subtitles/SRTs",
    ".sub": "Videos/Subtitles/SUBs",
    ".vtt": "Videos/Subtitles/VTTs",
}

# Music & Lyrics extensions
MUSIC_EXT_MAP: Dict[str, str] = {
    ".mp3": "Music/MP3s",
    ".wav": "Music/WAVs",
    ".flac": "Music/FLACs",
    ".opus": "Music/OPUSs",
    ".aac": "Music/AACs",
    ".m4a": "Music/M4As",
    ".lrc": "Music/LRCs",
}

# Archive extensions
ARCHIVE_EXT_MAP: Dict[str, str] = {
    ".zip": "Archives/ZIPs",
    ".rar": "Archives/RARs",
    ".7z": "Archives/7Zs",
    ".tar": "Archives/TARs",
    ".gz": "Archives/GZs",
}

# Other extensions: code, web, config, binaries, misc
OTHER_EXT_MAP: Dict[str, str] = {
    # Code / Notebooks
    ".py": "Project/Python",
    ".ipynb": "Project/Notebooks",
    ".sh": "Project/Scripts",
    ".ps1": "Project/Scripts",

    # Web / Frontend
    ".html": "WebPages",
    ".htm": "WebPages",
    ".css": "WebPages/CSS",
    ".js": "WebPages/JS",
    ".mjs": "WebPages/JS",
    ".ts": "WebPages/TS",
    ".jsx": "WebPages/JSX",
    ".tsx": "WebPages/TSX",

    # Markup / Docs
    ".md": "Documents/Text Files",
    ".rst": "Documents/Text Files",
    ".tex": "Documents/Text Files",
    ".epub": "Documents/EPUBs",

    # Config / Data
    ".xml": "Others/XML",
    ".yml": "Others/YAML",
    ".yaml": "Others/YAML",
    ".ini": "Others/Configs",
    ".cfg": "Others/Configs",
    ".sql": "Others/SQL",
    ".db": "Others/Databases",
    ".sqlite": "Others/Databases",

    # Images / Vector / Design
    ".svg": "Images/SVGs",
    ".psd": "Images/PSD",
    ".ai": "Images/Illustrator",

    # Binaries / Installers
    ".exe": "Others/Executables",
    ".msi": "Others/Executables",
    ".apk": "Others/APKs",
    ".bin": "Others/Binaries",
    ".dll": "Others/Binaries",
    ".iso": "Others/ISOs",

    # Misc
    ".vcf": "Others/Contacts",
    ".ics": "Others/Calendars",
    ".torrent": "Others/Torrents",
    ".bak": "Others/Backups",
}

# Individual category maps exposed for inspection / customization
CATEGORY_MAPS: Dict[str, Dict[str, str]] = {
    "Documents": DOC_EXT_MAP,
    "Images": IMG_EXT_MAP,
    "GIFs": GIF_EXT_MAP,
    "Videos": VIDEO_EXT_MAP,
    "Music": MUSIC_EXT_MAP,
    "Archives": ARCHIVE_EXT_MAP,
    "Others": OTHER_EXT_MAP,
}

# Merged map for O(1) lookup
ALL_EXTENSIONS: Dict[str, str] = {}
_ALL_MAPS = [
    DOC_EXT_MAP,
    IMG_EXT_MAP,
    GIF_EXT_MAP,
    VIDEO_EXT_MAP,
    MUSIC_EXT_MAP,
    ARCHIVE_EXT_MAP,
    OTHER_EXT_MAP,
]
for _m in _ALL_MAPS:
    ALL_EXTENSIONS.update(_m)
