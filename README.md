# Speech-to-Text-Transcription
# 🎤 Speech-to-Text Transcription

A Python-based Speech-to-Text application that converts spoken words into text using the **SpeechRecognition** library. The application captures audio through a microphone, transcribes it into text, displays the output on the screen, and saves the transcript to a text file.

---

## 📖 Project Overview

Speech-to-Text Transcription is a simple Python project that demonstrates how speech recognition technology can be used to convert human speech into written text. This project uses a microphone as the input source and Google's Speech Recognition API for transcription.

---

## ✨ Features

- 🎤 Capture voice input using a microphone
- 📝 Convert speech into text
- 💾 Save the transcribed text to a file (`output.txt`)
- ⚡ Fast and easy-to-use interface
- 🌐 Supports English speech recognition

---

## 🛠️ Technologies Used

- **Python 3**
- **SpeechRecognition**
- **PyAudio**
- **Google Speech Recognition API**

---

## 📂 Project Structure

```
Speech-to-Text-Transcription/
│── app.py
│── output.txt
│── requirements.txt
└── README.md
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Keerthi8970/Speech-to-Text-Transcription.git
```

### 2. Open the Project Folder

```bash
cd Speech-to-Text-Transcription
```

### 3. Install Required Libraries

```bash
pip install SpeechRecognition
pip install PyAudio
```

If you face issues installing PyAudio on Windows:

```bash
pip install pipwin
pipwin install pyaudio
```

---

## ▶️ Running the Project

Run the following command:

```bash
python app.py
```

The application will ask you to speak through your microphone.

---

## 📌 Example

### Input (Speech)

> Hello everyone. Welcome to my Speech-to-Text project.

### Output (Text)

```
Hello everyone.
Welcome to my Speech-to-Text project.
```

The recognized text is also saved in **output.txt**.

---

## 📸 Sample Output

```
===== Speech-to-Text Transcription =====

Speak now...

Processing...

You said:

Hello everyone.
Welcome to my Speech-to-Text project.

Transcript saved successfully to output.txt
```

---

## 📈 Future Enhancements

- 🌍 Multi-language speech recognition
- 🖥️ Graphical User Interface (GUI) using Tkinter
- 📄 Export transcripts to PDF and Word
- 🎧 Support for audio file transcription
- 🤖 Offline transcription using OpenAI Whisper
- ⚡ Real-time speech transcription

---

## 👩‍💻 Author

**Keerthi K R**

GitHub: https://github.com/Keerthi8970

---

## 📄 License

This project is created for educational and learning purposes.

---

⭐ **If you found this project useful, consider giving it a Star on GitHub!**
