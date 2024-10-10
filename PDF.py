from pypdf import PdfWriter
merger=PdfWriter()

for pdf in ["1sem.pdf","2sem.pdf","3sem.pdf","4sem.pdf"]:
    merger.append(pdf)
merger.write("New PDF.pdf")
merger.close()