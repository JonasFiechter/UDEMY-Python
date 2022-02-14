import os

caminho = 'D:/'
termo_procura = 'Ro'

for root, dirs, files in os.walk(caminho):
    # print(files)
    for file in files:
        print(file)
        caminho_completo = os.path.join(root, file)
        nome_arquivo, ext_arquivo = os.path.splitext(file)
        tamanho = os.path.getsize(caminho_completo)
        pass