# Python program to translate
# speech to text and text to speech
 
 
import socket 
import speech_recognition as sr
import pyttsx3

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
r = sr.Recognizer()

def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say("did you say " + command)
    engine.runAndWait()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    # s.setblocking(0)
    # s.settimeout(0)
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        try:
         
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                 
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                engine = pyttsx3.init()
                engine.say("Please say something. ")
                engine.runAndWait()

                print("Please say something. ")
                r.adjust_for_ambient_noise(source2, duration=0.2)

                
                #listens for the user's input
                audio2 = r.listen(source2)
                 
                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                print("Did you say "+MyText)
                SpeakText(MyText)
                tosend = bytes(MyText,'UTF-8')
                 
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
         
        except sr.UnknownValueError:
            print("unknown error occured")
        
        conn.sendall(tosend)