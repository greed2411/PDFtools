import os
import img2pdf

# takes all the images in the current working directory and puts as one centered image per page
with open("output.pdf", "wb") as f:
    f.write(img2pdf.convert([i for i in os.listdir(os.getcwd()) if i.endswith(".jpg")]))
