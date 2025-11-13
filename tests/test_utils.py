from pathlib import Path
from download_organizer.utils import  (
    get_download_path,
    get_documents_path,
    get_desktop_path,
    get_pictures_path,
    get_dev_path,
    ensure_folder_exists,
    join_path,
    get_file_extension,
    list_files_in_folder,
    list_folder_in_folder,
    get_unique_filename,
    safe_move_file,
    safe_copy_file
)

#Pruebo mis Path's:

print("\n")
print("\n")
print("Probamos nuestras rutas importantes: ")
print("\n")
print("\n")
print("\n")
print(get_download_path())
print(get_documents_path())
print(get_desktop_path())
print(get_pictures_path())
print(get_dev_path())
print("\n")
print("\n")
print("\n")


#Path para testear:

test_path = Path("C:/Users/Ezequiel/Dev/automation_scripts/Level 1 - Fundamentals/download_organizer/tests/tests_folder")

test_path_falso = Path("C:/Users/Ezequiel/Dev/automation_scripts/Level 1 - Fundamentals/download_organizer/tests/tests_folder/queonda.txt")
test_path_falso1 = Path("C:/Users/Ezequiel/Dev/automation_scripts/Level 1 - Fundamentals/download_organizer/tests/tests_folder/queonda")



print(test_path.exists())
print(test_path_falso.exists())
print(test_path_falso1.exists())


#Ahora vamos a garantizar que existan test_path_false y test_path_false1:

ensure_folder_exists(test_path_falso)
ensure_folder_exists(test_path_falso1)



print("\n")
print("\n")
print("\n")


test_path_1 = Path("C:/Users/Ezequiel/Dev/automation_scripts/Level 1 - Fundamentals/download_organizer/tests/tests_folder")

print(join_path(test_path_1, "document"))
print(join_path(test_path_1, "document3331", "hola333"))
print(join_path)

print("\n")
print("\n")
print("\n")


print(get_file_extension(join_path(test_path_1, "texto.txt")))
print(get_file_extension(join_path(test_path_1, "texto.py")))
print(get_file_extension(join_path(test_path_1, "texto.")))
print(get_file_extension(join_path(test_path_1, "texto")))

path_test = Path("C:/Users/Ezequiel/Dev/automation_scripts/Level 1 - Fundamentals/download_organizer/tests")
path_test_files =  Path("C:/Users/Ezequiel/Dev/automation_scripts/Level 1 - Fundamentals/download_organizer/tests/tests_folder")

# Solo txt y pdf
filter_parameters0 = ["txt", "pdf"]

# Imágenes y csv
filter_parameters1 = ["jpg", "png", "csv"]

# Lenguajes de programación
filter_parameters2 = ["py", "java", "c", "cpp", "js"]

print(list_files_in_folder(path_test))
print("\n")
print(list_files_in_folder(path_test_files))
print("\n")
print(list_files_in_folder(path_test_files, filter_parameters0))
print("\n")
print(list_files_in_folder(path_test_files, filter_parameters1))
print("\n")
print(list_files_in_folder(path_test_files, filter_parameters2))




print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")


print(list_folder_in_folder(path_test_files))


print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")


"""path_file_1_false = Path("C:/Users/Ezequiel/Dev/automation_scripts/Level 1 - Fundamentals/download_organizer/tests/tests_folder")
path_file_1 = Path("C:/Users/Ezequiel/Dev/automation_scripts/Level 1 - Fundamentals/download_organizer/tests/tests_folder/file0s.txt")

print(get_unique_filename(path_file_1_false))
print(get_unique_filename(path_file_1_false))
ddd = get_unique_filename(path_file_1_false)
print(get_unique_filename(path_file_1_false))
ddd.touch(exist_ok=True)
print(get_unique_filename(path_file_1_false))

print("\n")

print(get_unique_filename(path_file_1))
print(get_unique_filename(path_file_1))
fff = get_unique_filename(path_file_1)
print(get_unique_filename(path_file_1))
fff.touch()
print(get_unique_filename(path_file_1))"""



path_move1 = Path("C:/Users/Ezequiel/Dev/automation_scripts/Level 1 - Fundamentals/download_organizer/tests/tests_folder/mover1/texto.txt")
path_move2 = Path("C:/Users/Ezequiel/Dev/automation_scripts/Level 1 - Fundamentals/download_organizer/tests/tests_folder/mover2")


safe_move_file(path_move2, path_move1)