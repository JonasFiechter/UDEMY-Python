import os
import shutil

top = r'C:\Users\USER\Desktop'
n_top = r'C:\Users\USER\Desktop\TEST'
n2_top = r'C:\Users\USER\Desktop\TEST2'

try:
    os.mkdir(n_top)
except FileExistsError as f1:
    print(f'O caminho já existe: {FileExistsError.__name__}')

try:
    os.mkdir(n2_top)
except FileExistsError as f1:
    print(f'O caminho já existe: {FileExistsError.__name__}')

count = 0
for root, dirs, files in os.walk(n_top):
    for file in files:
        old_path = os.path.join(root, file)
        new_path = os.path.join(n2_top, file)

        if '.png' in file:
            shutil.copy(old_path, new_path)
            print(f'File: "{file}" copied successfully')
            count += 1

print(f'{count} files copied')