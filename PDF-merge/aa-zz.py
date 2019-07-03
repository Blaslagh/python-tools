import PyPDF2

#Opening both files

pdf1File = open('1.pdf', 'rb')
pdf2File = open('2.pdf', 'rb')

pdf1Reader = PyPDF2.PdfFileReader(pdf1File, strict=False)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File, strict=False)

#Creating new object to store pages

pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    #adding pages from both files
    pdfWriter.addPage(pdf1Reader.getPage(pageNum))
    pdfWriter.addPage(pdf2Reader.getPage(pageNum))

#Saving new pdf file
pdfOutputFile = open('merged.pdf', 'wb')
pdfWriter.write(pdfOutputFile)

#Clearing the mess

pdfOutputFile.close()
pdf1File.close()
pdf2File.close()