Overview
This project is designed to control a robotic arm using voice commands. It utilizes the pyFirmata library to interface with an Arduino and control the servo motors attached to various joints of the robotic arm. Speech recognition is handled using the SpeechRecognition library, and text-to-speech is managed by pyttsx3.

Requirements
Python 3.x
Arduino with servos connected to the appropriate pins
pyFirmata
pyttsx3
SpeechRecognition
word2number
Arduino StandardFirmata firmware uploaded to the Arduino board
Installation
Clone the repository:

sh
Copy code
git clone <repository-url>
cd <repository-directory>
Install the required packages:

sh
Copy code
pip install pyfirmata pyttsx3 SpeechRecognition word2number
Upload StandardFirmata to Arduino:

Open the Arduino IDE.
Go to File -> Examples -> Firmata -> StandardFirmata.
Upload the StandardFirmata sketch to your Arduino board.
Hardware Setup
Connect your Arduino to the computer.
Connect the servos to the appropriate pins on the Arduino:
Base servo: Pin 9
Shoulder servo: Pin 10
Elbow servo: Pin 11
Wrist servo: Pin 12
Grip servo: Pin 13
Running the Application
Connect your Arduino to the computer.

Run the Python script:

sh
Copy code
python app.py
Application Usage
Voice Commands
The application will prompt you to specify which servo pin to operate.
You can say the pin number (e.g., "nine" for the base servo).
The application will then prompt you for the angle.
You can say the desired angle (e.g., "forty-five").
The servo will rotate to the specified angle.

Code Explanation
Main Functions
word_to_number(word):

Converts a spoken number word to an integer.
speak(audio):

Uses pyttsx3 to convert text to speech.
takeCmd():

Listens for a voice command and returns the recognized string.
rotateServo(pin, angle):

Rotates the specified servo to the given angle.
Main Application Flow
Initialize the Arduino and Servos:
Setup the servo pins using pyFirmata.
Text-to-Speech Initialization:
Initialize pyttsx3 for speech output.
Voice Command Processing:
Prompt the user for the servo pin.
Listen and convert the spoken pin to a corresponding integer.
Prompt the user for the angle.
Listen and convert the spoken angle to a corresponding float.
Servo Control:
Continuously rotate the servo to the specified angle based on voice commands.
Example Usage
Example Voice Commands
Pin Selection:

"Tell us the pin you wanna operate with"
User says: "nine"
Angle Selection:

"Angle please"
User says: "forty-five"
Servo Movement
The base servo (pin 9) will rotate to 45 degrees.
Notes
Make sure the Arduino is connected to the correct COM port specified in the code ('COM3' in the example).
Ensure the baud rate matches the settings on your Arduino (115200 in the example).
You can adjust the COM port and pin numbers in the code as needed.
For accurate voice recognition, ensure you are in a quiet environment and speak clearly.
Troubleshooting
Serial Connection Issues:
Verify the correct COM port is used.
Ensure no other applications are using the same COM port.
Voice Recognition Issues:
Ensure your microphone is working properly.
Test with a different microphone if necessary.
Ensure you have an active internet connection for the Google Speech Recognition API.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

