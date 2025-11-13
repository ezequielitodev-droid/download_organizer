import logging
import os
import shutil
from pathlib import Path
from dotenv import load_dotenv

#Cargamos funciones de entorno:

load_dotenv()

#Configuramos los Logging:

format = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger_move = logging.getLogger("mover")
logger_move.setLevel(logging.INFO)

fh_move = logging.FileHandler(f"{os.getenv("SAFE_MOVE_FILE_LOG")}", encoding="utf-8" )
fh_move.setLevel(logging.INFO)

fh_move.setFormatter(format)

logger_move.addHandler(fh_move)



logger_copy = logging.getLogger("copiar")
logger_copy.setLevel(logging.INFO)

fh_copy = logging.FileHandler(f"{os.getenv("SAFE_COPY_FILE_LOG")}", encoding="utf-8")
fh_copy.setLevel(logging.INFO)

fh_copy.setFormatter(format)

logger_copy.addHandler(fh_copy)


# Funciones para obtener los path's

def get_download_path() -> Path: 
    
    """
    Return the path to the download folder as a Path object.

    This function reads the environment variable 'DOWNLOAD_PATH' to get the
    user's download folder. If the environment variable is not set, it falls
    back to the default 'Downloads' folder inside the user's home directory.

    Returns
    -------
    Path
        A pathlib.Path object pointing to the download folder.

    Examples
    --------
    >>> from pathlib import Path
    >>> path = get_download_path()
    >>> isinstance(path, Path)
    True
    >>> path.exists()  # The folder may or may not exist yet
    True or False
    """
    
    path = os.getenv("DOWNLOAD_PATH")

    if path:
        path = Path(path)
    else:
        path = Path.home() / "Download"
    
    return path

def get_documents_path() -> Path:

    """
    Return the path to the documents folder as a Path object.

    This function reads the environment variable 'DOCUMENTS_PATH' to get the
    user's documents folder. If the environment variable is not set, it falls
    back to the default 'Documents' folder inside the user's home directory.

    Returns
    -------
    Path
        A pathlib.Path object pointing to the documents folder.

    Examples
    --------
    >>> from pathlib import Path
    >>> path = get_documents_path()
    >>> isinstance(path, Path)
    True
    >>> path.exists()  # The folder may or may not exist yet
    True or False
    """
    
    path = os.getenv("DOCUMENTS_PATH")

    if path:
        path = Path(path)
    else:
        path = Path.home() / "Documents"
    
    return path

def get_desktop_path() -> Path:

    """
    Return the path to the desktop folder as a Path object.

    This function reads the environment variable 'DESKTOP_PATH' to get the
    user's desktop folder. If the environment variable is not set, it falls
    back to the default 'Desktop' folder inside the user's home directory.

    Returns
    -------
    Path
        A pathlib.Path object pointing to the desktop folder.

    Examples
    --------
    >>> from pathlib import Path
    >>> path = get_desktop_path()
    >>> isinstance(path, Path)
    True
    >>> path.exists()  # The folder may or may not exist yet
    True or False
    """
    
    path = os.getenv("DESKTOP_PATH")

    if path:
        path = Path(path)
    else:
        path = Path.home() / "Desktop"
    
    return path

def get_pictures_path() -> Path:

    """
    Return the path to the pictures folder as a Path object.

    This function reads the environment variable 'PICTURES_PATH' to get the
    user's pictures folder. If the environment variable is not set, it falls
    back to the default 'Pictures' folder inside the user's home directory.

    Returns
    -------
    Path
        A pathlib.Path object pointing to the pictures folder.

    Examples
    --------
    >>> from pathlib import Path
    >>> path = get_pictures_path()
    >>> isinstance(path, Path)
    True
    >>> path.exists()  # The folder may or may not exist yet
    True or False
    """

    
    path = os.getenv("PICTURES_PATH")

    if path:
        path = Path(path)
    else:
        path = Path.home() / "Pictures"
    
    return path

def get_dev_path() -> Path:

    """
    Return the path to the development folder as a Path object.

    This function reads the environment variable 'DEV_PATH' to get the
    user's development folder. If the environment variable is not set, it falls
    back to the default 'Dev' folder inside the user's home directory.

    Returns
    -------
    Path
        A pathlib.Path object pointing to the development folder.

    Examples
    --------
    >>> from pathlib import Path
    >>> path = get_dev_path()
    >>> isinstance(path, Path)
    True
    >>> path.exists()  # The folder may or may not exist yet
    True or False
    """
    
    path = os.getenv("DEV_PATH")

    if path:
        path = Path(path)
    else:
        path = Path.home() / "Dev"
    
    return path

# Funciones de verificacion:

def ensure_folder_exists(path: Path) -> None:

    """
    Ensure that the folder at the given path exists.
    If it does not exist, create it along with any necessary parent folders.

    Parameters
    ----------
    path : Path
        The folder path to ensure exists.

    Returns
    -------
    None

    Examples
    --------
    >>> from pathlib import Path
    >>> test_path = Path("C:/Users/Ezequiel/TestFolder/Subfolder")
    >>> ensure_folder_exists(test_path)
    >>> test_path.exists()
    True
    >>> test_path.is_dir()
    True
    """

    path.mkdir(parents=True, exist_ok=True)

# Funciones de manipulacion de rutas:

def join_path(base: Path, *sub_folders: str) -> Path:

    """
    Safely join base path with one or more subfolders.

    Parameters
    ----------
    base : Path
        The base path.
    *subfolders : str
        One or more folder names to combine.

    Returns
    -------
    Path
        The combined path.

    Examples
    --------
    >>> from pathlib import Path
    >>> join_path(Path("C:/Users/Ezequiel"), "Documents", "Proyectos")
    WindowsPath('C:/Users/Ezequiel/Documents/Proyectos')
    """

    for sub in sub_folders:
        base = base / sub
    
    return base

def get_file_extension(file: Path) -> str:

    """
    Return the file extension of a given file as a string.

    Parameters
    ----------
    file : Path
        The file path to extract the extension from.

    Returns
    -------
    str
        The file extension without the leading dot.
        Returns an empty string if the file has no extension.

    Examples
    --------
    >>> from pathlib import Path
    >>> f = Path("C:/Users/Ezequiel/test.txt")
    >>> get_file_extension(f)
    'txt'
    >>> f2 = Path("C:/Users/Ezequiel/README")
    >>> get_file_extension(f2)
    ''
    """

    return file.suffix[1:] if file.suffix else ""

# Funciones de filtrado y de busqueda:

def list_files_in_folder(folder: Path, extensions: list[str] | None = None) -> list[Path]:
    
    """
    List all files in a given folder, optionally filtering by file extensions.

    Parameters
    ----------
    folder : Path
        The Path object representing the folder to search for files.
    extensions : list[str] | None, optional
        A list of file extensions to filter by (without leading dot), e.g. ["txt", "pdf"].
        If None (default), all files are returned.

    Returns
    -------
    list[Path]
        A list of Path objects corresponding to the files in the folder.
        If extensions are provided, only files matching the extensions are included.

    Examples
    --------
    >>> from pathlib import Path
    >>> folder = Path("C:/Users/Ezequiel/Downloads")
    >>> list_files_in_folder(folder)
    [Path('file1.txt'), Path('file2.pdf'), Path('image.jpg')]
    >>> list_files_in_folder(folder, ["txt", "pdf"])
    [Path('file1.txt'), Path('file2.pdf')]
    """

    ext_with_dot = [f".{ext.lower()}" for ext in extensions] if extensions else None

    return [
        f for f in folder.iterdir()
        if (f.is_file()) and ((ext_with_dot is None) or (f.suffix.lower() in ext_with_dot))
    ]

def list_folder_in_folder(folder: Path) -> list[Path]:

    """
    List all subfolders in a given folder.

    Parameters
    ----------
    folder : Path
        The Path object representing the folder to search for subfolders.

    Returns
    -------
    list[Path]
        A list of Path objects corresponding to the subfolders in the folder.

    Examples
    --------
    >>> from pathlib import Path
    >>> folder = Path("C:/Users/Ezequiel/Downloads")
    >>> list_folder_in_folder(folder)
    [Path('C:/Users/Ezequiel/Downloads/Proyectos'),
     Path('C:/Users/Ezequiel/Downloads/Imagenes')]
    """

    return [
        f for f in folder.iterdir()
        if (f.is_dir())
    ]

# Funciones para mover y organizar sin sobreescribir nada:

def get_unique_filename(file: Path) -> Path:
    
    """
    Generate a unique file path in the same directory, avoiding overwriting existing files.

    Parameters
    ----------
    file : Path
        The original file path.

    Returns
    -------
    Path
        A Path object pointing to a unique file name in the same directory.
        If the original file does not exist, returns it unchanged.
        Otherwise, appends a counter in parentheses, e.g., 'file(1).txt', 'file(2).txt', etc.

    Examples
    --------
    >>> from pathlib import Path
    >>> f = Path("C:/Users/Ezequiel/Documents/photo.jpg")
    >>> get_unique_filename(f)  # Suppose photo.jpg exists
    WindowsPath('C:/Users/Ezequiel/Documents/photo(1).jpg')

    >>> get_unique_filename(f) # Suppose photo(2).jpg exists
    WindowsPath('C:/Users/Ezequiel/Documents/photo(2).jpg')

    >>> f2 = Path("C:/Users/Ezequiel/Documents/photo(1).jpg")
    >>> get_unique_filename(f2)  # Suppose photo(1).jpg exists
    WindowsPath('C:/Users/Ezequiel/Documents/photo(1)(1).jpg')
    """

    temp_file = file

    if file.exists():
        
        parent = file.parent
        stem = file.stem
        suffix = file.suffix

        counter = 1
        flag = True

        while flag:

            new_name = f"{stem}({counter}){suffix}"
            new_path = parent / new_name

            if not new_path.exists():
                temp_file = new_path
                flag = False
            
            counter += 1

    return temp_file

def safe_move_file(src: Path, dst: Path) -> None:

    """
    Safely move a file to a destination path while preventing accidental overwrites
    and avoiding operations on directories.

    This function moves a file from `src` to `dst`. If `dst` is a directory, the file
    is placed inside it using its original filename. If a file with the same name
    already exists at the destination, a unique filename is generated automatically
    via `get_unique_filename()` to prevent overwriting.

    Several safety checks are enforced:
    - The source path must exist.
    - The destination path must exist.
    - The source must not be a directory. If it is, the operation is aborted.
    - If the destination is a directory, the final target path becomes `dst/src.name`.

    The move operation is handled by `shutil.move()`. Any issues such as missing paths
    or unexpected errors are logged. Directory sources trigger a warning and are not moved.

    Parameters
    ----------
    src : Path
        The source file path.
    dst : Path
        The destination path or directory.

    Notes
    -----
    - If `src` does not exist, a warning is logged and nothing is moved.
    - If `dst` does not exist, the function logs a warning and stops.
    - If `src` is a directory, an `IsADirectoryError` is raised and logged, and the
      operation is aborted.
    - Unique filenames are handled by `get_unique_filename()`.
    - All warnings and errors are logged using `logger_move`.

    Examples
    --------
    >>> safe_move_file(Path("Downloads/photo.jpg"), Path("Documents/"))
    # Moves 'photo.jpg' into Documents, generating a unique name if needed.

    >>> safe_move_file(Path("Downloads/photo.jpg"), Path("Documents/photo.jpg"))
    # Moves to the exact file target, renaming if the file already exists.
    """


    try:

        if not src.exists(): raise FileNotFoundError(f"Sorce does not exist: {src}")

        if not dst.exists(): raise FileNotFoundError(f"Destination folder does not exist: {dst}")

        if src.is_dir(): raise IsADirectoryError(f"Source is a directory, not a file: {src}")

        if dst.is_dir(): dst = dst / src.name

        shutil.move(src, get_unique_filename(dst))

        logger_move.info(f"File moved successfully: {src} -> {dst}")

    except FileNotFoundError as e:
        
        logger_move.warning(f"Error moving file: {e}")
    
    except IsADirectoryError as e:

        logger_move.warning("Source path is a directory. Operation aborted.")

    except Exception as e:
        
        logger_move.error(f"An unexpected error occurred while moving file: {e}")



def safe_copy_file(src: Path, dst: Path) -> None: 
    
    """
    Copy a file safely to a destination path, ensuring no existing files are overwritten.

    This function copies a file from `src` to `dst`. If `dst` is a folder, the file is
    placed inside it with its original name. If a file with the same name already exists
    in the destination, a unique name is generated automatically using `get_unique_filename()`.

    The copy operation is performed using `shutil.copy2()`, which preserves metadata such as
    modification time.

    Parameters
    ----------
    src : Path
        The source file to be copied.
    dst : Path
        The destination file path or directory.

    Notes
    -----
    - If `src` does not exist, the function logs a warning and stops.
    - If `dst` does not exist, the function logs a warning and stops.
    - If `dst` is a file path, the copied file will replace only the filename part.
    - `get_unique_filename()` ensures the resulting file path is unique.
    - All outcomes (success, warnings, errors) are written to the log.

    Examples
    --------
    >>> from pathlib import Path
    >>> safe_copy_file(Path("C:/Users/Ezequiel/Downloads/photo.jpg"),
    ...                Path("C:/Users/Ezequiel/Documents/"))
    # Copies 'photo.jpg' into the Documents folder, renaming if needed.

    >>> safe_copy_file(Path("C:/Users/Ezequiel/Downloads/photo.jpg"),
    ...                Path("C:/Users/Ezequiel/Documents/photo.jpg"))
    # Copies the file to an explicit path, generating a unique name if needed.
    """
    
    try:
    
        if not src.exists(): raise FileNotFoundError(f"Source does not exist: {src}")
        
        if not dst.exists(): raise FileNotFoundError(f"Destination folder does not exist: {dst}")

        if dst.is_dir(): dst = dst / src.name

        shutil.copy2(src, get_unique_filename(dst))

        logger_copy.info(f"File copied successfully: {src} -> {dst}")

    except FileNotFoundError as e:

        logger_copy.warning(f"File copy failed: {e}")

    except Exception as e:

        logger_copy.error(f"Unexpected error while copying file: {e}")