# HRI_SemesterProject_2022Spring
 This project is a turn taking robot game in which the child tries to guess a number based on the feedback from the robot. 


Necessary Libraries: 
Python 3.12: 
    socket 
    speech_recognition as sr
    pyttsx3
    json 
    playsound
    time 

Webots R2022a

Choregraphe 2.8.6 (Windows or Intel MAC Only)

First, make sure you have the necessary python packages installed locally and the right version of Webots installed. Webots does not recognize any virtual environments. If you won't be creating any other motion files, you won't need Choregraphe. It is only to facilitate the process of creating motion files. Finally, download the source codes as they are. 

1. Run the speech recognition server using the following terminal command: python3 sr.py
2. Click on project.wbt in the main directory
3. Click on the play button at the top of the screen. 
5. Enjoy the game. :)

When playing, once the robot reads the directions to you, press a key for the game to continue. This was something we had to do because the simulator does not allow the sleep function. 