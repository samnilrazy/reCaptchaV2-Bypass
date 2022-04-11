from pydub import AudioSegment
import speech_recognition as sr 

# files                                                                       
src = "payload.mp3"
dst = "wav.wav"

# convert wav to mp3                                                            
audSeg = AudioSegment.from_mp3("payload.mp3")
audSeg.export(dst, format="wav")
filename = 'wav.wav'

r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print("O Conteudo é: {}".format(text))
