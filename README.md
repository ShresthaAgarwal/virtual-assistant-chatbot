# virtual-assistant-chatbot
# Speech Recognition and Response System

Overview:
This program is designed to recognize speech input from the user and respond accordingly. It utilizes the speech_recognition library to recognize speech and the pyttsx3 library for text-to-speech conversion.

Requirements:
1. Python 3.x
2. speech_recognition library
3. pyttsx3 library
4. Usage
5. Install the required libraries using pip:

Copy code:
1. pip install SpeechRecognition pyttsx3
2. Run the script.
3. Speak into the microphone when prompted.
4. The program will recognize your speech and respond accordingly.

Functionality:
Recognize Speech: 
The program listens for input from the microphone and converts it into text using Google Speech Recognition.

Respond to User:
Based on the user input, the program generates an appropriate response. Here are some supported queries and their responses:

"hello": "Hello, how can I help you?"
"name": "My name is shivangi"
"courses": "IPEC have 3 courses which are B.tech , BBA , BCA"
"course duration": "Our college offers 4 year long B.tech course and 3 year long BBA & BCA course."
"location": "Site-IV Sahibabad Ghaziabad ,Uttar Pradesh"
"semDuration": "The single semester will be around 4 months."
"joke": "Why did the tomato turn red? Because it saw the salad dressing!"
"bye": "See you" (Terminates the program)

Main Loop:
The program runs in an infinite loop, continuously listening for user input. It terminates upon receiving the "bye" command.
