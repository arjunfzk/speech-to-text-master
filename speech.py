# -*- coding: utf-8 -*-

from gtts import gTTS
 
# This module is imported so that we can 
# play the converted audio
import os
 
# The text that you want to convert to audio
mytext = 'जैसे मैं सेब सेब सेब सेब पसंद करता हूं मुझे संतरे नारंगी संतरे संतरे पसंद हैं मुझे केले केले केले केले केले केले पसंद करती है केले केले मुझे कीवी कीवी कीवी कीवी पसंद है I अंगूर अंगूर अंगूर अंगूर की तरह मैं अंगूरों का जीरा पसंद करता हूं मुझे चेरी चेरी चेरी चेरी पसंद है मुझे नींबू की नींबू नींबू नींबू पसंद है'
mytext=str(mytext)
print(mytext)
file = open("testfile.txt","w",encoding='utf-8')
file.write(mytext)
file = open("testfile.txt", "r",encoding='utf-8') 
x=file.read()  
language = 'hi'
print(x)
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=x, lang=language, slow=False)
 
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")
 