import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define a function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        # Use Google Speech Recognition to transcribe audio
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

# Define a function to speak text aloud
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Main loop to handle user input and respond
while True:
    input_text = recognize_speech()
    if input_text is not None:
        print("You said: " + input_text)
        # Process user input and generate a response
        if "hello" in input_text.lower():
            response_text = "Hello, how can I help you?"
        elif "name" in input_text.lower():
            response_text="My name is shivangi"
        elif "courses" in input_text.lower():
            response_text="IPEC have 3 courses which are B.tech , BBA , BCA"
        elif "course duration" in input_text.lower():
            response_text="Our college offers 4 year long B.tech course and 3 year long BBA & BCA course."
        elif "Location" in input_text.lower():
            response_text="Site-IV Sahibabad Ghaziabad ,Uttar Pradesh"
        elif "semDuration" in input_text.lower():
            response_text="The single semester will be around 4 months."
        elif "joke" in input_text.lower():
            response_text = "Why did the tomato turn red? Because it saw the salad dressing!"
        elif "bye" in input_text.lower():
            response_text = "See you"
            speak_text(response_text)
            print("Response:"+ response_text)
            break
        else:
            response_text = "I'm sorry, I didn't understand. Could you please repeat?"
        speak_text(response_text)
        print("Response:"+ response_text)
