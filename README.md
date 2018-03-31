# PDFtools

A set of scripts which make handling PDFs easier. Works on all platforms. Tested on **Ubuntu 16.10** and **Win 7 32 bit SP1** with **Python 3.6.0 | Anaconda 4.3.1**

### Dependency

  * [PyPDF2](https://pypi.python.org/pypi/PyPDF2/1.26.0) v1.26.0 - To read and merge the PDFs.
  * [img2pdf](https://pypi.python.org/pypi/img2pdf) v0.2.4 - To read images and merge as PDF.

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

## images2pdf

Script to create a PDF with all the images in the current working directory.

### Usage

Open Terminal where the **script** and the **images** are present and run the *images2pdfgenereator.py*

**Note:** script supports both .jpg and .png formats only. Haven't tested with any other formats.

```
λ python images2pdfgenerator.py
Enter output filename: test
Done.
λ
```
