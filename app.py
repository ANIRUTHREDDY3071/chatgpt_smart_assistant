import openai
from apikey import api_data

import os
import speech_recognition as sr 
import pyttsx3 #readout text output 
import webbrowser 

# Set the correct model name
Model = "gpt-4"

# Initialize the OpenAI client with the API key
client = openai(api_key=api_data)

def Reply(question):
    # Create a chat completion
    completion = client.chat.completions.create(
        model=Model,
        messages=[
            {'role': "system", "content": "You are a helpful assistant."},
            {'role': 'user', 'content': question}
        ],
        max_tokens=200
    )
    
    # Get the assistant's response
    answer = completion.choices[0].message['content']
    return answer

# Define a question to ask the model
#question = "In simple terms, explain AI in no more than 50 words."

# Get the answer from the model
#ans = Reply(question)

# Print the result
#print(ans)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("hello how are you aniruth reddy")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening..')
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        print("recognizing.....")
        query = r.recognize_google(audio,language = 'en-in')
        print("user said:{} \n".format(query))
    except Exception as e:
        print ("say that again...")
        return "None"
    return query 



if __name__=="__main__":
    while True:
        query = takeCommand().lower()
        if query == "none":
            continue 

        ans = Reply(query)
        print(ans)
        speak(ans)

        if "Open Youtube " in query:
            webbrowser.open('www.youtube.com')

        if "Open Google" in query:
            webbrowser.open('www.google.com')

        if "bye" in query:
            break
