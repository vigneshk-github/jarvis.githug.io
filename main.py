from Brain.AIBrain import ReplayBrain
from Body.speak import speak
from Body.listen import takecommand

# if __name__ == "__main__":
def runJarvis():
    speak("Hello sir")
    while True:
        query = takecommand()
        if query == "None":
            speak("Please say that again")
        else:
            answer = ReplayBrain(query)
            speak(answer)
