# pip install gTTS
from gtts import gTTS
import os

# The text that you want to convert to audio
text1 = "Advanced Data Structures is the best subject we have"
text2 = "Por favor que el parcial de ADS no sea muy difícil"

# Google's API code
audio = gTTS(text=text1, lang="en", slow=False)

# Saving the converted audio in a mp3 file named prueba
audio.save("prueba.mp3")

# Playing the converted file
os.system("prueba.mp3")