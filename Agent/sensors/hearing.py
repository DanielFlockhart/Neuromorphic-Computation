
import speech_recognition as sr


class Ear:
    def __init__(self):
        self.name = 'ear'
        self.type = 'sensor'
        self.status = 'functional'

    def get_status(self):
        return self.status
    
    def recieve(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                return text
            except:
                return None


if __name__ == "__main__":
    ear = Ear()
    print(ear.recieve())