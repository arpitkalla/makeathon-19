import speech_recognition as sr
import pyaudio 
from threading import Thread
import requests

url = "http://localhost:5000/move/"
direction = "n"
sentRequest = True


"""
listen to user statement in mic
returns spoken words from user OR 
returns empty string if source not detected
"""
def listen(r, mic):
  with mic as source:
    r.adjust_for_ambient_noise(source)
    print("\n\n\nYou may begin talking:\n\n\n") #testing
    audio = r.listen(source)
  
  try:
    return r.recognize_google(audio)

  except sr.UnknownValueError:
    print ("What are you saying?") #testing
    return ""


class ListenThread(Thread):
  def __init__(self):
    Thread.__init__(self)

  def run(self):
    while True:
      global direction, setnRequest
      r = sr.Recognizer()
      
      ### opens microphone and takes speech from human to convert to text
      mic = sr.Microphone(0)
      spoken_text = listen(r, mic)
      if (spoken_text == "start"):
        direction = "r"
        sentRequest = False
      else:
        print(spoken_text)

            
thread = ListenThread()
thread.start()

while True:
  if direction != "" and sentRequest == False:
    requests.get(url + direction)
    

