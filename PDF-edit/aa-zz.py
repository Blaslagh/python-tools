import PyPDF2

pdf1File = open('1.pdf', 'rb')
pdf2File = open('2.pdf', 'rb')

pdf1Reader = PyPDF2.PdfFileReader(pdf1File, strict=False)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File, strict=False)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pdfWriter.addPage(pdf1Reader.getPage(pageNum))
    pdfWriter.addPage(pdf2Reader.getPage(pageNum))

pdfOutputFile = open('C:/Users/Adam/Desktop/razem.pdf', 'wb')
pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()
pdf1File.close()
pdf2File.close()