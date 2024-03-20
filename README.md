# virtual-assistant-chatbot
#Speech Recognition and Response System

Overview
This program is designed to recognize speech input from the user and respond accordingly. It utilizes the speech_recognition library to recognize speech and the pyttsx3 library for text-to-speech conversion.

Requirements
Python 3.x
speech_recognition library
pyttsx3 library
Usage
Install the required libraries using pip:

Copy code
pip install SpeechRecognition pyttsx3
Run the script.

Speak into the microphone when prompted.

The program will recognize your speech and respond accordingly.

Functionality
Recognize Speech: The program listens for input from the microphone and converts it into text using Google Speech Recognition.

Respond to User: Based on the user input, the program generates an appropriate response. Here are some supported queries and their responses:

"hello": "Hello, how can I help you?"
"name": "My name is shivangi"
"courses": "IPEC have 3 courses which are B.tech , BBA , BCA"
"course duration": "Our college offers 4 year long B.tech course and 3 year long BBA & BCA course."
"location": "Site-IV Sahibabad Ghaziabad ,Uttar Pradesh"
"semDuration": "The single semester will be around 4 months."
"joke": "Why did the tomato turn red? Because it saw the salad dressing!"
"bye": "See you" (Terminates the program)
Main Loop
The program runs in an infinite loop, continuously listening for user input. It terminates upon receiving the "bye" command.
