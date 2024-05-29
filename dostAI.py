import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()

#
text_to_speech = pyttsx3.init()

#function to open a specific website
def open_website(url):
    webbrowser.open(url)

#function to make the AI speak
def speak(text):
    text_to_speech.say(text)
    text_to_speech.runAndWait()

#function to recognize and run voice commands
def recognize_voice_command():
    listening = False  
    taking_notes = False  

    while True:
        with sr.Microphone() as source:
            if listening:
                print("Listening for a command...")
                audio = recognizer.listen(source)
            else:
                print("Say 'dost' to start listening, 'exit' to quit, 'start note' to begin note-taking, or 'stop note' to end note-taking.")
                audio = recognizer.listen(source, timeout=10)  # Wait for  voice command for  10 seconds

        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)

            if "dost" in command:
                listening = True
                speak("AI is awake and listening.")
            elif "exit" in command:
                speak("Exiting the AI.")
                break
            elif "start note" in command:
                taking_notes = True
                speak("Starting note-taking. Please speak your notes.")
                notes = []
            elif "stop note" in command:
                taking_notes = False
                speak("Stopping note-taking. Saving your notes.")
                if notes:
                    with open("notes.txt", "a") as f:
                        for note in notes:
                            f.write(note + "\n")
                    notes = []
                else:
                    speak("No notes to save.")
            elif listening and taking_notes:
                notes.append(command)
                print("Note: ", command)
            elif listening:
                if "open facebook" in command:
                    open_website("https://www.facebook.com")
                    speak("Opening Facebook.")
                elif "open instagram" in command:
                    open_website("https://www.instagram.com")
                    speak("Opening Instagram.")
                elif "open youtube" in command:
                    open_website("https://www.youtube.com")
                    speak("Opening YouTube.")
                elif "open fiver" in command:
                    open_website("https://www.fiver.com")
                    speak("Opening fiver.")
                elif "open discord" in command:
                    open_website("https://www.discord.com")
                    speak("Opening discord.")
                else:
                    speak("Command not recognized.")

        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

if __name__ == "__main__":
    recognize_voice_command()
