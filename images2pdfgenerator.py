import os
import img2pdf

filename = input("Enter output filename: ")
if '.pdf' not in filename: filename = filename + '.pdf'

with open(filename, "wb") as f:
    f.write(img2pdf.convert([i for i in os.listdir(os.getcwd()) if i.endswith(".png") or i.endswith(".jpg")]))

print("Done. ")