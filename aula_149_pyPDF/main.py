import PyPDF2
import os

caminho_pdf = r'C:\Users\USER\Downloads'

novo_pdf = PyPDF2.PdfFileMerger()
for root, dirs, files in os.walk(caminho_pdf):
    for file in files:
        caminho_pdf_full = os.path.join(root, file)
        if 'pdf' in file:
            arquivo_pdf = open(caminho_pdf_full, 'rb')
            novo_pdf.append(arquivo_pdf)