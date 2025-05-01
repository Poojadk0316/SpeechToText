# speech_to_text.py

import speech_recognition as sr

def recognize_speech(timeout=8):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("🎙️ Listening...")
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=8)
            text = recognizer.recognize_google(audio)
            return text
        except sr.WaitTimeoutError:
            print("⏳ No speech detected within timeout.")
            return ""
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            return f"Speech recognition error: {e}"
