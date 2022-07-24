import time
from PIL import Image
import numpy as np

file=open("pixel.txt","r")
pixels=[]
st=time.time()
while(True):
    line=file.readline()
    # if(line==""):
    #     break
    txt=line.split()
    if(len(txt)==2):
        w=int(txt[0])
        h=int(txt[1])
        break
    else:
        txt[0]=int(txt[0])
        txt[1]=int(txt[1])
        txt[2]=int(txt[2])
        pixels.append(txt)


# print(pixels)
# print("W=="+str(w))
# print("H=="+str(h))
count=0

img=Image.new('RGB',(w,h))
for i in range(0,h):
    for j in range(0,w):
        # print(count)
        pix=pixels[count]
        img.putpixel((i,j), (pix[0],pix[1],pix[2]))
        count=count+1

img.save('sqr.png')
et=time.time()
print("Time=",et-st)