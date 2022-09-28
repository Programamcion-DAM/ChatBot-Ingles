import speech_recognition as sr

class VoiceRecognizer:
    def __init__(self):
        self.r= sr.Recognizer()
        self.mic = sr.Microphone(device_index=3)

    def hear(self):
        with self.mic as source:
            print("\n(···)",end=" ")
            self.r.adjust_for_ambient_noise(source, duration=0.2)
            audio = self.r.listen(source)
        print(";)\n")

        try:
            text = self.r.recognize_google(audio)
        except:
            print("Oh, parece que no te he entendido bien :(")
            return self.hear()
        
        return text

"""

Este codigo sirve para saber que device_index poner.
Debe elegir el numero que le corresponde a su microfono.

i = 1
for micro in sr.Microphone.list_microphone_names():
    print(i,": ",micro)
    i = i+1
"""