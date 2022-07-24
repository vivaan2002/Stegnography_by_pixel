import time
import audioconverter
import audioreader
import audiowriter
st=time.time()

# audioconverter.mp3towav('EncodeAudio/test1.mp3','EncodeAudio/output.wav')

# audioreader.audiotoimage('EncodeAudio/output.wav')

audiowriter.imagetoaudio('image.png','DecodeAudio/final.wav')

audioconverter.wavtomp3('DecodeAudio/final.wav','DecodeAudio/final.mp3')
et=time.time()
print("Time=",et-st)


