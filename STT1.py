import speech_recognition as sr
from pydub import AudioSegment
# assign files
input_file = 'shish.wav'
output_file = "result.wav"
  
# convert mp3 file to wav file
sound = AudioSegment.from_mp3(input_file)
sound.export(output_file, format="wav")

r = sr.Recognizer()
with sr.WavFile('result.wav') as source:
    audio = r.record(source)
text = r.recognize_google(audio)
print(text)
