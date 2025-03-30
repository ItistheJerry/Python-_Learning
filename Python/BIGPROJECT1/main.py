import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import musicLibrary



recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
   if "open google" in c.lower():
      webbrowser.open("https://google.com")
   elif "open FaceBook" in c.lower():
      webbrowser.open("https://facebok.com")
   elif "open Youtube" in c.lower():
      webbrowser.open("https://youtube.com")
   elif c.lower().startswith("play"):
      song = c.lower().split(" ")[1]
      link = musicLibrary.music[song]
      webbrowser.open(link)
   elif "news" in c.lower():
       pass


if __name__ == "__main__": 
    speak("I am Maa, Your Personnal Assistant! The Full Form is Morden Artificial Assistant")
    while True:
     # Listen for the wake work MON
     # Obtain audio from the microphone.

    #  r = sr.Recognizer()



    
     # Recognize speech using google
     print("Recogninzing....")
     try:
         with sr.Microphone() as source:
          print("Listening...")
          recognizer.adjust_for_ambient_noise(source, duration=1)
          audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
         command = recognizer.recognize_google(audio)
         
         
         if command and command == "hello":
            speak("Yes BOSS")
            with sr.Microphone() as source:
               print("Your Maa is active and I am Listening.....")
               recognizer.adjust_for_ambient_noise(source, duration=1)
               audio = recognizer.listen(source, timeout=10, phrase_time_limit=8)
               command = recognizer.recognize_google(audio).lower()
               print(f"Executing Command: {command}")


               processCommand(command)


            #  Listening for Command
        #  print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    #  except Exception as e:
    #      print("Error; {0}".format(e))

     except sr.UnknownValueError:
            print("Sorry, I couldn't understand that. Try speaking louder or closer to the mic.")
            print(f"Captured Audio: {audio}")

     except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition: {e}")
     except Exception as e:
            print(f"An error occurred: {e}")