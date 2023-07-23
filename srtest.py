import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source: # device_index=2
    r.adjust_for_ambient_noise(source, duration=5)
    print("input>:")
    audio = r.listen(source, phrase_time_limit=4)
    #print("received")
# with sr.AudioFile('exampleaudio.wav') as source:
#     audio = r.listen(source)

# recognize speech using whisper
try:
    print(">: " + r.recognize_whisper(audio, language="english"))
except sr.UnknownValueError:
    print("Whisper could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Whisper")

# recognize speech using Sphinx
#try:
#    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
#except sr.UnknownValueError:
#    print("Sphinx could not understand audio")
#except sr.RequestError as e:
#    print("Sphinx error; {0}".format(e))
