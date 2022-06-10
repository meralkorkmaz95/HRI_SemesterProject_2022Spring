# Python program to translate
# speech to text and text to speech
 
 
import socket 
import speech_recognition as sr
import pyttsx3
import json 
from playsound import playsound
import time 

HOST = "127.0.0.1"  
PORT = 65432  
r = sr.Recognizer()
r.energy_threshold = 4000
engine = pyttsx3.init()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))        
s.listen()
conn, addr = s.accept()
print(f"Connected by {addr}")
engine.say("Let's play a game. I am going to think of a number. You try to guess it, and I will tell you if you are correct. ")
engine.runAndWait()
time.sleep(1)
finish = False
while(1): 
    data = conn.recv(1024)
    if not data: break

    msg = json.loads(data)
    if msg["stage"] == "guess": 
        try:
            # use the microphone as source for input.
                with sr.Microphone() as source:
                     
                    # wait for a second to let the recognizer
                    # adjust the energy threshold based on
                    # the surrounding noise level
                    engine.say("Make a guess!")
                    engine.runAndWait()

                    print("Make a guess!")
                    r.adjust_for_ambient_noise(source, duration=1)

                    
                    #listens for the user's input
                    audio2 = r.listen(source)
                     
                    # Using google to recognize audio
                    MyText = r.recognize_google(audio2)
                    MyText = MyText.lower()

                    print(MyText + "is a good guess. ")

                    if int(MyText) < int(msg["goal"]): 
                        engine.say(MyText + " is a good guess. Try something higher. ")
                    elif int(MyText) > int(msg["goal"]): 
                        engine.say(MyText + " is a good guess. Try something lower. ")
                    else: 
                        engine.say(MyText + " is correct. Way to go. ")
                        finish = True
                    engine.runAndWait()

                    
                    tosend = bytes(MyText,'UTF-8')
                     
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
         
        except sr.UnknownValueError:
            print("unknown error occured")
        
        conn.sendall(tosend)
        if(finish): 
            playsound('macarena.wav')
