#!/usr/bin/env python3

import os
import re
import sys
from transliterate import translit

def sanitize_filename(filename):
    filename = filename.replace(' ', '-')
    filename = translit(filename, 'ru', reversed=True)
    filename = re.sub(r'[^a-zA-Zа-яА-Я0-9-]', '-', filename)
    filename = re.sub(r'-+', '-', filename)
    return filename.strip('-')

def rename_files_and_directories(root_dir):
    # Переименование файлов
    for current_root, dirs, files in os.walk(root_dir):
        renamed_files = []  # список новых имён для текущей папки

        for filename in files:
            name, ext = os.path.splitext(filename)
            new_name = sanitize_filename(name) + ext.lower()
            old_path = os.path.join(current_root, filename)
            new_path = os.path.join(current_root, new_name)

            if old_path != new_path:
                os.rename(old_path, new_path)
                print(f"Файл: '{old_path}' -> '{new_path}'")

            renamed_files.append(new_name)

        # создаём лог в текущей папке
        if renamed_files:
            log_path = os.path.join(current_root, "rename_log.txt")
            with open(log_path, "w", encoding="utf-8") as log_file:
                log_file.write("\n".join(renamed_files))
            print(f"Лог создан: {log_path}")

    # Переименование папок
    for current_root, dirs, files in os.walk(root_dir, topdown=False):
        for dirname in dirs:
            old_dir = os.path.join(current_root, dirname)
            new_dirname = sanitize_filename(dirname)
            new_dir = os.path.join(current_root, new_dirname)
            if old_dir != new_dir:
                os.rename(old_dir, new_dir)
                print(f"Папка: '{old_dir}' -> '{new_dir}'")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Укажите папку для переименования!")
        sys.exit(1)

    directory_path = sys.argv[1]
    rename_files_and_directories(directory_path)
