import PyPDF2
from pathlib import Path
import os

dirpath = os.getcwd()

pathlist = Path(dirpath).glob('**/*.pdf')
for path in pathlist:
    #path não é uma string!
    path_in_str = str(path)
    print(path_in_str)
    pdfFileObj = open(path_in_str, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    texto = ''

    for i in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(i)
        texto += pageObj.extractText()
    
    path_txt = path_in_str.replace('.pdf', '.txt')
    with open(path_txt, 'w') as f:  
        f.write(texto) 