import speech_recognition as sr
# Build the AI
class ChatBot():
    def __init__(self, name):
        print("--- starting up", name, "---")
        self.name = name
    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
             print("listening...")
             audio = recognizer.listen(mic)
        try:
             self.text = recognizer.recognize_google(audio)
             print("me --> ", self.text)
        except:
             print("me -->  ERROR")
    def wake_up(self,text):
        return True if self.name in text.lower() else False





# Run the AI
if __name__ == "__main__":    
    ai = ChatBot(name="maya")
    while True:
         ai.speech_to_text()
