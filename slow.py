# -*- coding: utf-8 -*-

import os
import speech_recognition as sr
from tqdm import tqdm

import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='api-key.json'




with open("api-key.json") as f:
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()

r = sr.Recognizer()
files = os.listdir('parts/')

all_text = []

for f in tqdm(files):
    name = "parts/" + f
    # Load audio file
    with sr.AudioFile(name) as source:
        audio = r.record(source)
    # Transcribe audio file
    text = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
    all_text.append(text)

transcript = ""
for i, t in enumerate(all_text):
    total_seconds = i * 30
    # Cool shortcut from:
    # https://stackoverflow.com/questions/775049/python-time-seconds-to-hms
    # to get hours, minutes and seconds
    m, s = divmod(total_seconds, 60)
    h, m = divmod(m, 60)

    # Format time as h:m:s - 30 seconds of text
    transcript = transcript + "{:0>2d}:{:0>2d}:{:0>2d} {}\n".format(h, m, s, t)

print(transcript)

from google.cloud import translate

    # Instantiates a client
translate_client = translate.Client()

    # The text to translate
    # The target language
text=transcript
target = 'hi'

    # Translates some text into Russian
translation = translate_client.translate(
text,
target_language=target)

print(u'Text: {}'.format(text))
print(u'Translation: {}'.format(translation['translatedText']))


translation=translation['translatedText']

translation=str(translation)


file = open("testfile.txt","w",encoding='utf-8')
file.write(translation)
file = open("testfile.txt", "r",encoding='utf-8') 
x=file.read()  





#print(type(translation))
from gtts import gTTS
 
# This module is imported so that we can 
# play the converted audio
import os
 
# The text that you want to convert to audio
mytext = x[8:]
language = 'hi'
 
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
 
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")
 

"""
with open("transcript.txt", "w") as f:
    f.write(transcript)
"""