import PyPDF2


# mergeFile = PyPDF2.PdfMerger()
#
# mergeFile.append(PyPDF2.PdfReader('pdf-1.pdf'))
# mergeFile.append(PyPDF2.PdfReader('pdf-2.pdf'))
#
# mergeFile.write("new-merged-pdf.pdf")


# another way...
def merge_pdfs(_pdfs):
    merge_file = PyPDF2.PdfMerger()

    for _pdf in _pdfs:
        merge_file.append(PyPDF2.PdfReader(_pdf))

    merge_file.write("new-merged-pdf.pdf")


if __name__ == '__main__':
    _pdfs = ['pdf-1.pdf', 'pdf-2.pdf', 'pdf-3.pdf']
    merge_pdfs(_pdfs)
