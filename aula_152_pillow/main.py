import os
from PIL import Image


def main(folder):
    if not os.path.isdir(folder):
        raise NotADirectoryError(f'Caminho {folder} não encontrado.')

    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
            new_file, extension = os.path.splitext(file)
            new_file = file_name + '_CONVERTED' + extension


if __name__ == '__main__':
    main(folder=r'C:\Users\USER\Pictures')