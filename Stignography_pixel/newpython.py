from ast import Str
import time
from PIL import Image
st=time.time()
# img = input("Enter image name(with extension) : ")
img="./Pdf/pdf_secret.png"
image = Image.open(img, 'r')
file=open("pixel.txt","w+")

imgdata = iter(image.getdata())

w,h=image.size
run=w*h
c=0
while (c<run):
    pixels = [value for value in imgdata.__next__()[:3]]
    c=c+1
    # print(pixels)
    file.write(str(pixels[0])+" ")
    file.write(str(pixels[1])+" ")
    file.write(str(pixels[2])+" ")
    file.write("\n")

file.write(str(w)+" "+str(h))
file.close()

et=time.time()
print("Time=",et-st)

    # if (pixels[-1] % 2 != 0):
    #     break
 
    # # string of binary data
    # binstr = ''
 
    # for i in pixels[:8]:
    #     if (i % 2 == 0):
    #         binstr += '0'
    #     else:
    #         binstr += '1'
 