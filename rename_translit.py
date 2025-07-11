import os
import re
from transliterate import translit  # pip install transliterate

def sanitize_filename(filename):
    filename = filename.replace(' ', '-')
    filename = translit(filename, 'ru', reversed=True)
    filename = re.sub(r'[^a-zA-Zа-яА-Я0-9-]', '-', filename)
    filename = re.sub(r'-+', '-', filename)
    return filename.strip('-')

def rename_files_and_directories(root_dir):
    for current_root, dirs, files in os.walk(root_dir):
        for filename in files:
            old_path = os.path.join(current_root, filename)
            name, ext = os.path.splitext(filename)
            new_name = sanitize_filename(name) + ext.lower()
            new_path = os.path.join(current_root, new_name)
            if old_path != new_path:
                os.rename(old_path, new_path)
                print(f"Файл: '{old_path}' -> '{new_path}'")

    for current_root, dirs, files in os.walk(root_dir, topdown=False):
        for dirname in dirs:
            old_dir = os.path.join(current_root, dirname)
            new_dirname = sanitize_filename(dirname)
            new_dir = os.path.join(current_root, new_dirname)
            if old_dir != new_dir:
                os.rename(old_dir, new_dir)
                print(f"Папка: '{old_dir}' -> '{new_dir}'")

if __name__ == "__main__":
    directory_path = os.getcwd()
    rename_files_and_directories(directory_path)

