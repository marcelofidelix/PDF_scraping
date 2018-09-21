import PyPDF2
pdfFileObj = open('a.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

texto = ''

for i in range(pdfReader.numPages):
	pageObj = pdfReader.getPage(i)
	texto += pageObj.extractText()

print(texto)

