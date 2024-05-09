import os
from PyPDF2 import PdfReader

def extrair_texto_pdfs_em_diretorio(diretorio):
    texto_completo = ''
    for nome_arquivo in os.listdir(diretorio):
        if nome_arquivo.endswith('.pdf'):
            caminho_pdf = os.path.join(diretorio, nome_arquivo)
            texto_completo += extrair_texto_pdf(caminho_pdf)
    return texto_completo

def extrair_texto_pdf(caminho_pdf):
    texto_completo = ''
    with open(caminho_pdf, 'rb') as arquivo_pdf:
        leitor_pdf = PdfReader(arquivo_pdf)
        num_paginas = len(leitor_pdf.pages)

        for pagina_numero in range(num_paginas):
            pagina = leitor_pdf.pages[pagina_numero]
            texto_completo += pagina.extract_text()

    return texto_completo

# Exemplo de uso
diretorio_de_pdfs = '../../bo'
texto_extraido = extrair_texto_pdfs_em_diretorio(diretorio_de_pdfs)
print(texto_extraido)
