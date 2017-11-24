try : 
    from PyPDF2 import PdfFileMerger
except ImportError:
    raise ImportError('** Install PyPDF2 **')
import os


path = input("Enter the path to the pdf files : ")
output = input("Enter output filename : ")

os.chdir(path)

pdfs = [f for f in os.listdir(path) if f.endswith('.pdf')]

print('Wait...')

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open('{}.pdf'.format(output), 'wb') as fout:
    merger.write(fout)

print('Done xD')