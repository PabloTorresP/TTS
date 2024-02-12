# Text-to-speech (TTS)
Advance Data Structures
# Text-to-Speech Converter

This simple Python script demonstrates how to use the `gTTS` library to convert text to speech and play it back. It uses Google's Text-to-Speech API to generate audio files from text input.

## Installation

You can install the necessary library using pip:
pip install gTTS



## How to Use

1. **Install gTTS Library**: If you haven't already, install the `gTTS` library using pip.
2. **Open the Script**: Open the Python script in your preferred code editor.
3. **Replace Sample Text**: Replace the sample text in the script with the text you want to convert to audio.
4. **Run the Script**: Execute the Python script in your terminal or code editor.
5. **Generated Audio File**: After running the script, a file named `prueba.mp3` will be created in the same directory as the script.
6. **Playback**: The script will automatically play back the generated audio.

##Note

Make sure you have an internet connection while running the script as it requires access to Google's Text-to-Speech API.

## Example

```python
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
