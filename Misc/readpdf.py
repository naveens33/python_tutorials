import PyPDF2

pdf_file = open('C:\\Users\\naveen.s\\Downloads\\8534567-01-10-12.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
print(str(page_content.encode('utf-8')))
print ("1127593857803" in str(page_content.encode('utf-8')))