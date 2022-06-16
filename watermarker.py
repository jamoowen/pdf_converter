import PyPDF2
import sys


# opens the watermark via first cmd line arg
# opens pdf file to be watermarked via second arg
with open(sys.argv[2], 'rb') as pdf, open(sys.argv[1], 'rb') as water:
    original_pdf = PyPDF2.PdfFileReader(pdf)
    watermark = PyPDF2.PdfFileReader(water)
    watermark_page = watermark.getPage(0)

    
    output = PyPDF2.PdfFileWriter() 

    # loops through pages in orgininal pdf and merges the watermarked page
    for i in range(original_pdf.getNumPages()):
        page = original_pdf.getPage(i)
        page.mergePage(watermark_page)
        output.addPage(page)

    # writes the new pdf to a filename
    with open('merged.pdf', 'wb') as merged:
        output.write(merged)
    
