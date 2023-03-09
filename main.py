import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()

with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text via google speech recognition
    text = r.recognize_google(audio_data)
    print(text)
    # convert speech to text via pocket sphinx
    # text = r.recognize_sphinx(audio_data)
    # print(text)

