import os
import moviepy.video.io.ImageSequenceClip
image_folder='tmp1'
fps=24
count =288
image_files=[]
for img in range(0,288):
    image_files.append(str(img)+".png")
image_files = [os.path.join(image_folder,img)
               for img in image_files]
print(image_files)
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile('new_video.mp4')