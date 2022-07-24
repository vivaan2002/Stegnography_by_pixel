path=r"D:\py_module_external\poppler-22.04.0\Library\bin"
import time
from pdf2image import convert_from_path
 
st= time.time() 
# Store Pdf with convert_from_path function
images = convert_from_path(pdf_path='testpdf.pdf',poppler_path=path)
 
for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save('./temp/page'+ str(i) +'.png', 'PNG')

et = time.time()
print("Time=",et-st)