import img2pdf
from PIL import Image
import os

# storing image path
img_path = "./temp/page"

# storing pdf path
pdf_path = "file.pdf"
# opening or creating pdf file
file = open(pdf_path, "wb")
for x in range(0,5):
    img_p=img_path+str(x)+".png" 
    # opening image
    image = Image.open(img_p)

    # converting into chunks using img2pdf
    pdf_bytes = img2pdf.convert(image)

    # writing pdf files with chunks
    file.write(pdf_bytes)

    # closing image file
    image.close()

# closing pdf file
file.close()

# output
print("Successfully made pdf file")
