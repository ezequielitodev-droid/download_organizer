from download_organizer.utils import (
    get_documents_path,
    get_pictures_path,
    get_audio_path,
    get_video_path,
    get_archives_path, 
    get_code_path, 
    get_executables_path
)


# Maps each file extension to a category name
extension_to_category = {
    # Documents
    ".pdf": "documents",
    ".doc": "documents",
    ".docx": "documents",
    ".txt": "documents",
    ".odt": "documents",
    ".rtf": "documents",
    ".xlsx": "documents",
    ".xls": "documents",
    ".csv": "documents",
    ".ppt": "documents",
    ".pptx": "documents",

    # Pictures
    ".jpg": "pictures",
    ".jpeg": "pictures",
    ".png": "pictures",
    ".gif": "pictures",
    ".bmp": "pictures",
    ".svg": "pictures",
    ".webp": "pictures",

    # Audio
    ".mp3": "audio",
    ".wav": "audio",
    ".flac": "audio",
    ".aac": "audio",
    ".ogg": "audio",

    # Video
    ".mp4": "video",
    ".avi": "video",
    ".mov": "video",
    ".mkv": "video",
    ".wmv": "video",

    # Compressed files
    ".zip": "archives",
    ".rar": "archives",
    ".7zip": "archives",
    ".tar": "archives",
    ".gz": "archives",

    # Code / development
    ".py": "code",
    ".js": "code",
    ".java": "code",
    ".c": "code",
    ".cpp": "code",
    ".cs": "code",
    ".html": "code",
    ".css": "code",
    ".json": "code",
    ".xml": "code",
    ".yml": "code",
    ".yaml": "code",

    # Executables / installers
    ".exe": "executables",
    ".msi": "executables",
    ".apk": "executables",
    ".bat": "executables",
    ".sh": "executables",
    ".spec": "executables",

    # Disk images
    ".iso": "disk_images",
}



category_to_path = {
    "documents": get_documents_path(), 
    "pictures": get_pictures_path(), 
    "audio": get_audio_path(), 
    "video": get_video_path(), 
    "archives": get_archives_path(),
    "code": get_code_path(),
    "executables": get_executables_path()
}



TEMPORARY_EXTENSIONS = [".crdownload", ".part", ".tmp"]