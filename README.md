
# Voice Controlled Robotic Arm

This project implements a voice-controlled robotic arm using an Arduino and Python. The arm can be manipulated via voice commands to control its servos, as well as execute additional tasks like searching Wikipedia, opening websites, and reporting the current time.

## Overview

### Features
- **Voice Control**: Control the robotic arm's servos by speaking commands.
- **Multi-Tasking**: Execute various tasks such as fetching information from Wikipedia, opening websites, and reporting the current time.

## Requirements

- Python 3.x
- pyfirmata
- pyttsx3
- speech_recognition
- word2number
- pyaudio
- Arduino board

## Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <repository_name>
   ```

2. Install the required packages:
   ```sh
   pip install pyfirmata pyttsx3 SpeechRecognition word2number pyaudio
   ```

## Running the Application

1. Connect your Arduino to the computer.
2. Upload the necessary firmware to your Arduino board.
3. Run the main application:
   ```sh
   python main.py
   ```

## Code Explanation

### Main Functions
- `speak(audio)`: Uses the pyttsx3 library to convert text to speech and speak it aloud.
- `takeCmd()`: Listens for a voice command from the user and returns the recognized string.
- `rotateServo(pin, angle)`: Rotates the servo connected to the specified pin to the given angle.

### Main Application Flow
1. **Servo Initialization**:
   ```python
   board.digital[base]=SERVO #base
   board.digital[shoulder]=SERVO #shoulder
   board.digital[elbow]=SERVO #elbow
   board.digital[wrist]=SERVO #wrist
   board.digital[grip]=SERVO #grip
   ```
2. **Voice Command Handling**:
   - The user is prompted to specify the servo pin and angle to control the robotic arm.
   - The application listens for commands and executes the corresponding actions.

3. **Additional Functionality**:
   - Implements commands for searching Wikipedia, opening web pages, and reporting the current time.

## Example Usage
- **Voice Commands**:
  - "Rotate servo 10 degrees"
  - "Open YouTube"
  - "What is the time?"

## Notes
- Ensure the Arduino is connected to the correct COM port specified in the code ('COM3' in the example).
- Adjust the servo pins in the code as per your setup.

## Troubleshooting

### Common Issues:
- **Voice Recognition**: If the speech recognition does not work, check your microphone settings and ensure the environment is quiet.
- **Servo Movement**: Ensure the servos are correctly connected and powered.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

---

# pyttsx Voice Module Tutorial

This tutorial covers the installation and usage of the pyttsx3 voice synthesis library in Python. The pyttsx3 library allows you to convert text into speech.

## Overview

### Features
- Text-to-speech functionality for various applications.
- Support for different voices and speech rates.

## Requirements

- Python 3.x
- pyttsx3
- pyaudio

## Installation

1. Install the required packages:
   ```sh
   pip install pyttsx3 pyaudio
   ```

## Usage

### Example Code
```python
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello, I am your voice assistant.")
```

### Customizing Voice Properties
- **Change Voice**:
  ```python
  engine.setProperty('voice', voices[1].id)  # Use second voice
  ```
- **Change Rate**:
  ```python
  rate = engine.getProperty('rate')
  engine.setProperty('rate', rate - 50)  # Decrease the speaking rate
  ```

## Notes
- The voice options may vary based on the operating system and installed voices.

## Troubleshooting

### Common Issues:
- **Voice Not Working**: Ensure your audio output device is functioning correctly and not muted.
- **Installation Errors**: Make sure to install all dependencies properly.

## License
This tutorial is licensed under the MIT License. See the LICENSE file for more details.

