import speech_recognition as sr
r= sr.Recognizer()
import speak
with sr.Microphone() as source:
    print ('say something')
    audio = r.listen(source)

try:
    text =r.recognize_google(audio)
    text2=("hello"+r.recognize_google(audio))
    print('Google thinks you said:\n'+r.recognize_google(audio))
    lang ='en'
    speak.tts(text,lang)
    if(r.recognize_google(audio)=="hello"):
        print("say back hello")
except:
    pass
