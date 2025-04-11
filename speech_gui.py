import tkinter as tk
import speech_recognition as sr
import threading
import time

def recognize_speech():
    def listen_with_countdown():
        # Show countdown
        for i in range(3, 0, -1):
            output_label.config(text=f"Starting in {i}...")
            root.update()
            time.sleep(1)

        recognizer = sr.Recognizer()
        recognizer.energy_threshold = 50  # Sensitive to soft voices
        recognizer.dynamic_energy_threshold = False

        with sr.Microphone() as source:
            output_label.config(text="🎙 Listening...")
            root.update()

            try:
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=6)
                text = recognizer.recognize_google(audio, language='en-US')
                output_label.config(text="You said:\n" + text)
            except sr.UnknownValueError:
                output_label.config(text="Sorry, couldn't understand the audio.")
            except sr.RequestError:
                output_label.config(text="Could not request results from the service.")
            except Exception as e:
                output_label.config(text="Error: " + str(e))

    threading.Thread(target=listen_with_countdown).start()

# Set up GUI
root = tk.Tk()
root.title("Speech to Text")
root.geometry("400x300")

speak_button = tk.Button(root, text="Speak", command=recognize_speech, font=("Arial", 14))
speak_button.pack(pady=20)

output_label = tk.Label(root, text="Click 'Speak' and start talking...", wraplength=350, font=("Arial", 12))
output_label.pack(pady=10)

root.mainloop()