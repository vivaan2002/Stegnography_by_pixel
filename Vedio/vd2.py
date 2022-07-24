from stegano import lsb
from os.path import isfile,join
import moviepy.video.io.ImageSequenceClip

import time
import cv2
import numpy as np
import math
import os
import shutil
from subprocess import call,STDOUT
count = 0

def vedio_former():
    image_folder='tmp1'
    fps=24
    image_files=[]
    for img in range(0,count):
        image_files.append(str(img)+".png")
    image_files = [os.path.join(image_folder,img)
                for img in image_files]
    print(image_files)
    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
    clip.write_videofile('my_video.mp4')


def split_string(s_str,count=10):
    per_c=math.ceil(len(s_str)/count)
    c_cout=0
    out_str=''
    split_list=[]
    for s in s_str:
        out_str+=s
        c_cout+=1
        if c_cout == per_c:
            split_list.append(out_str)
            out_str=''
            c_cout=0
    if c_cout!=0:
        split_list.append(out_str)
    return split_list

def frame_extraction(video):
    if not os.path.exists("./tmp1"):
        os.makedirs("tmp1")
    temp_folder="./tmp1"
    print("[INFO] tmp directory is created")

    vidcap = cv2.VideoCapture(video)
    count = 0

    while True:
        success, image = vidcap.read()
        if not success:
            break
        cv2.imwrite(os.path.join(temp_folder, "{:d}.png".format(count)), image)
        count += 1
    print("[INFO] farme extract completed")


def decode_string(video):
    frame_extraction(video)
    secret=[]
    root="./tmp/"
    for i in range(len(os.listdir(root))):
        f_name="{}{}.png".format(root,i)
        secret_dec=lsb.reveal(f_name)
        if secret_dec == None:
            break
        secret.append(secret_dec)
        
    print(''.join([i for i in secret]))

def main():
    input_string = input("Enter the input string :")
    f_name=input("enter the name of video")
    frame_extraction(f_name)
    

    
    
    # vedio_former()
if __name__ == "__main__":
    while True:
        print("1.Hide a message in video 2.Reveal the secret from video")
        print("any other value to exit")
        choice = input()
        if choice == '1':
            main()
        elif choice == '2':
            decode_string(input("enter the name of video with extension"))
        else:
            break
