import PyPDF2
import sys

pdfs = sys.argv[1:]

def combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
        print(pdf)

    merger.write('super.pdf')

combiner(pdfs)

