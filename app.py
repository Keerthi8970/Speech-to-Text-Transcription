import speech_recognition as sr

# Create recognizer
recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.pause_threshold = 1.0

print("\n===== Speech-to-Text Transcription =====\n")

# Display available microphones
mic_list = sr.Microphone.list_microphone_names()

print("Available Microphones:")
for i, mic in enumerate(mic_list):
    print(f"{i}: {mic}")

print("\nUsing default microphone...\n")

try:
    with sr.Microphone() as source:
        print("Please remain silent for 2 seconds...")
        recognizer.adjust_for_ambient_noise(source, duration=2)

        print("\nSpeak now (you have up to 10 seconds)...")

        audio = recognizer.listen(
            source,
            timeout=10,
            phrase_time_limit=10
        )

        print("Processing...")

    # Convert speech to text
    text = recognizer.recognize_google(audio, language="en-IN")

    print("\n========== RESULT ==========")
    print(text)

    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(text)

    print("\nTranscript saved successfully to output.txt")

except sr.WaitTimeoutError:
    print("\nNo speech detected. Please speak louder.")

except sr.UnknownValueError:
    print("\nSpeech was not recognized. Please speak clearly.")

except sr.RequestError as e:
    print("\nInternet connection error.")
    print(e)
except Exception as e:
    print("\nUnexpected Error:")
    print(e)

    