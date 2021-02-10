from gtts import gTTS
import os
tts = gTTS(text='This is Showrav.Nice to meet you. Have a nice day. Thank you!', lang='en')
tts.save("good.mp3")
os.system("good.mp3")