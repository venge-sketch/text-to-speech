from gtts import  gTTS
import os

fh=open('text.txt','r')
mytext= fh.read().replace('/n',' ')

language = "en"
output = gTTS(text= mytext,lang =language ,slow =False)

output.save('output.mp3')

os.system ('start output.mp3')
fh.close()