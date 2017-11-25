# PDFtools

A set of scripts which make handling PDFs easier. Works on all platforms. Tested on **Ubuntu 16.10** and **Win 7 32 bit SP1** with **Python 3.6.0 | Anaconda 4.3.1**

### Dependency

  * [PyPDF2](https://pypi.python.org/pypi/PyPDF2/1.26.0) v1.26.0 - To read and merge the PDFs.

## merger
Script to merge PDFs
  
### Usage

Open Terminal where the **script** is present

```
 $ python pdfmerger.py 
Enter the path to the pdf files : /media/greed/Windows8_OS/Me/Files/VIT/FALLSEM_17-18/OS
Enter output filename : osfatportions
Wait...
Done xD
 $ 
```

## subset
Script to create a PDF which is a subset of the original PDF.

### Usage

Open Terminal where the **script** is present, make sure the script and the pdf file are in the ***same directory***.

**Note :** when you give 6-13, it includes 6, 13 and all the numbers inbetween them. 

```
 $ python subset.py
Enter the name of the pdf : osfatportions
Enter the slicing : 1-3 6-13 16 19-20
Enter output filename : splitted
Wait...
Processing 498 pages...
Returning 14 pages...
Done.
 $ 

```
