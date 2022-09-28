from gtts import gTTS
from playsound import playsound
import os 

class SpeechPlayer:
    def __init__(self):
        pass
    
    def say(self,text):
        myobj = gTTS(text=text, lang='en', slow=False)
        myobj.save("response.mp3")
        playsound("response.mp3")
        os.remove("response.mp3")



