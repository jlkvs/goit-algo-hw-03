import os
import shutil
import argparse
from pathlib import Path

def parse_folder(path, dest_dir):
    
    for element in path.iterdir():
        if element.is_dir():
            print(f"Parse folder: This is folder - {element.name}")
            parse_folder(element, dest_dir)  
        if element.is_file():
            print(f"Parse folder: This is file - {element.name}")

            ext = element.suffix[1:].lower() if element.suffix else 'no_extension'
            ext_dir = Path(dest_dir) / ext

            ext_dir.mkdir(parents=True, exist_ok=True)

            dest_path = ext_dir / element.name
            shutil.copy2(element, dest_path)
            print(f'Копіюємо: {element} -> {dest_path}')

def main():
    parser = argparse.ArgumentParser(description='Копіює файли з директорії та сортує їх за розширеннями.')
    parser.add_argument('src_dir', help='Шлях до вихідної директорії.')
    parser.add_argument('dest_dir', nargs='?', default='dist', help='Шлях до директорії призначення (за замовчуванням "dist").')
    
    args = parser.parse_args()

    src_path = Path(args.src_dir)
    dest_path = Path(args.dest_dir)

    if not src_path.exists():
        print(f'Вихідна директорія "{src_path}" не існує.')
        return

    if not dest_path.exists():
        dest_path.mkdir(parents=True)
        print(f'Створено директорію призначення: {dest_path}')

    parse_folder(src_path, dest_path)
    print(f'Копіювання завершено у директорію: {dest_path}')

if __name__ == '__main__':
    main()
