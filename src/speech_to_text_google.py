import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please speak...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="en-IN")
        print("Recognized Text:", text)
    except sr.UnknownValueError:
        print("Speech could not be understood")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

if __name__ == "__main__":
    recognize_speech()
