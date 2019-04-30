#!/usr/bin/env python
from PyPDF2 import PdfFileReader, PdfFileWriter

def pdf_cat(input_files, output_stream):
    input_streams = []
    try:
        # First open all the files, then produce the output file, and
        # finally close the input files. This is necessary because
        # the data isn't read from the input files until the write
        # operation. Thanks to
        # https://stackoverflow.com/questions/6773631/problem-with-closing-python-pypdf-writing-getting-a-valueerror-i-o-operation/6773733#6773733
        for input_file in input_files:
            input_streams.append(open(input_file, 'rb'))
        writer = PdfFileWriter()
        for reader in map(PdfFileReader, input_streams):
            for n in range(reader.getNumPages()):
                writer.addPage(reader.getPage(n))
        output_file = open(output_stream, 'wb')
        writer.write(output_file)
    finally:
        for f in input_streams:
            f.close()

def main():
    # Get the file names
    file1 = input("Enter the name of the first file to combine: ")
    file2 = input("Enter the name of the second file to combine: ")
    files = [file1, file2]

    output = input("Enter the name of the output file (no extension): ") + ".pdf"

    pdf_cat(files, output)

main()
