try : 
    from PyPDF2 import PdfFileReader, PdfFileWriter
except ImportError:
    raise ImportError('** Install PyPDF2 **')


def processing_splitting(pages, num_of_pages, pdfReader, output):

    print('Wait...')
    print('Processing {} pages...'.format(num_of_pages))
    slicings = pages.split() # slicings = ['1-3', '6-13', '16', '19-20']
    pagesToObtain = []

    for slicing in slicings:
        
        page_indexes_str = slicing.split('-') # ['1', '3'] and ['16']

        try:
            beg, end = [ int(x) for x in page_indexes_str ] # for ['1', '3'] to [1, 3]
            pagesToObtain.append([i-1 for i in range(beg,end+1)])

        except ValueError:
            beg = [ int(x)-1 for x in page_indexes_str] # for ['16'] to [16-1(meaning 15)]
            pagesToObtain.append(beg)
        
    pagesFlattened = [ j for i in pagesToObtain for j in i]
    print('Returning {} pages...'.format(len(pagesFlattened)))
    # print(pagesFlattened) # causes [0, 1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 15, 18, 19]

    if all(i <= num_of_pages for i in pagesFlattened): # to check if numbers are lesser than total no. of pages
        
            pdfWriter = PdfFileWriter()
    
            # adding pages to pdf writer object
            for page in pagesFlattened:
                pdfWriter.addPage(pdfReader.getPage(page))
    
            # writing split pdf pages to pdf file
            with open('{}.pdf'.format(output), "wb") as f:
                pdfWriter.write(f)
            
            print('Done.')

    else :

        print('Slicings out of range.')

def gather_info():

    pdf_name = input('Enter the name of the pdf : ')
    if '.pdf' not in pdf_name:
        pdf_name = pdf_name + '.pdf'
    pdfFileObj = open(pdf_name, 'rb')
    pages = input('Enter the slicing : ') # pages = '1-3 6-13 16 19-20'
    pdfReader = PdfFileReader(pdfFileObj)
    num_of_pages = pdfReader.numPages
    output = input("Enter output filename : ")

    return pdf_name, pdfFileObj, pages, pdfReader, num_of_pages, output


def main():
    
    pdf_name, pdfFileObj, pages, pdfReader, num_of_pages, output = gather_info()
    processing_splitting(pages, num_of_pages, pdfReader, output)

if __name__ == '__main__':
    main()


            





