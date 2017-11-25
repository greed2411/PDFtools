try : 
    from PyPDF2 import PdfFileMerger
except ImportError:
    raise ImportError('** Install PyPDF2 **')
import os


def pdf_merge_action(pdfs, output):

    print('Wait...')
    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(open(pdf, 'rb'))

    with open('{}.pdf'.format(output), 'wb') as fout:
        merger.write(fout)
    print('Done xD')


def gather_info():

    path = input("Enter the path to the pdf files : ")
    os.chdir(path)
    output = input("Enter output filename : ")
    pdfs = [f for f in os.listdir(path) if f.endswith('.pdf')]
    return path, output, pdfs


def main():

    path, output, pdfs = gather_info()
    pdf_merge_action(pdfs, output)


if __name__ == '__main__':
    main()