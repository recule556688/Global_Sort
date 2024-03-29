MENU_CHOICE = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
]  # List of the menu choices
EXTENSIONS_MUSIC = {
    ".mp3": "Musique",
    ".wav": "Musique",
    ".flac": "Musique",
    ".ogg": "Musique",
    ".wma": "Musique",
    ".m4a": "Musique",
    ".aac": "Musique",
    ".aiff": "Musique",
    ".ape": "Musique",
}

EXTENSIONS_VIDEO = {
    ".mp4": "Videos",
    ".avi": "Videos",
    ".gif": "Videos",
    ".mkv": "Videos",
    ".wmv": "Videos",
    ".mov": "Videos",
}

EXTENSIONS_IMAGE = {
    ".bmp": "Images",
    ".png": "Images",
    ".jpg": "Images",
    ".JPG": "Images",
    ".jpeg": "Images",
    ".heic": "Images",
    ".svg": "Images",
}

EXTENSIONS_DOCUMENT = {
    ".txt": "Documents",
    ".pptx": "Documents",
    ".csv": "Documents",
    ".xls": "Documents",
    ".odp": "Documents",
    ".pages": "Documents",
    ".pdf": "Documents",
    ".doc": "Documents",
    ".zip": "Documents",
    ".docx": "Documents",
}

EXTENSIONS_DOWNLOAD = {
    ".exe": "executable",
    ".bat": "executable",
    ".sh": "executable",
    ".py": "executable",
    ".pyw": "executable",
    ".msi": "executable",
    ".apk": "executable",
    ".app": "executable",
    ".deb": "executable",
    ".rpm": "executable",
    ".bin": "executable",
    ".dmg": "executable",
    ".run": "executable",
    ".jar": "executable",
}

EXTENSIONS_PERSONNALISER = {
    ".ttf": "Fonts",
}

EXTENSIONS_ALL = {}
# Combine all the extension dictionaries into EXTENSIONS_DOWNLOAD
EXTENSIONS_ALL.update(EXTENSIONS_MUSIC)
EXTENSIONS_ALL.update(EXTENSIONS_VIDEO)
EXTENSIONS_ALL.update(EXTENSIONS_IMAGE)
EXTENSIONS_ALL.update(EXTENSIONS_DOCUMENT)
EXTENSIONS_ALL.update(EXTENSIONS_DOWNLOAD)
EXTENSIONS_ALL.update(EXTENSIONS_PERSONNALISER)

extension_dicts = [attr for attr in globals() if attr.startswith("EXTENSIONS_")]
folder_paths = {}
