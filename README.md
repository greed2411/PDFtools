# PDFtools

A set of scripts which make handling PDFs easier. Works across all platforms. Tested on **Pop! OS 20.04** and **Python 3.8.11**.

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
