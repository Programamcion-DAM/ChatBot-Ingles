from VoiceRecogntion import VoiceRecognizer
from Gpt3 import BotAI
from SpeechPlayer import SpeechPlayer
import os


user_name = input("Dime tu nombre: ")
os.system("cls")

recognizer = VoiceRecognizer()
talker = BotAI(user_name)
player = SpeechPlayer()

conversation = ""

while True:
    #Escuchamos al usuario
    user_input = recognizer.hear()
    
    #Juntamos la conversacion
    prompt = user_name + ": " + user_input + "\nAva:"
    conversation += prompt
    
    #Obtenemos la respuesta de la IA
    response = talker.talk(conversation)

    #Juntamos la respuesta a la conversacion
    conversation += response + "\n"

    #Mostramos y decimos la conversacion
    print(prompt,response,"\n")
    player.say(response)