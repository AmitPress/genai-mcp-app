# import libraries
import asyncio
import datetime
import speech_recognition as sr
import pyttsx3
from datetime import datetime
from mcp_client import agent
# Exceptions
class NullQueryException(Exception):
    pass

class Counter:
    value = 0
    def __init__(self, seed=0):
        self.value += seed
    def __call__(self, val=None):
        if not val:
            self.value += 1
        else:
            self.value += val
    def reset(self):
        self.value = 0
    

def speak_up(audio):
    engine.say(audio)
    engine.runAndWait()

def greetings():
    clock = int(datetime.now().hour)
    if clock>=6 and clock<12:
        speak_up("Good Morning")
    elif clock>=12 and clock<18:
        speak_up("Good Afternoon")
    elif clock>=18 and clock<24:
        speak_up("Good Evening")
    else:
        speak_up("Any Command Sir")

def get_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"Listening... ... ...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print(f"Processing... ... ...")
        query = r.recognize_google(audio, language='en-us')
        if not query:
            raise NullQueryException
    except NullQueryException:
        speak_up("No input found")
    except sr.UnknownValueError:
        query = None
    return query

async def main():
    count = Counter()
    async with agent.run_mcp_servers():
        while True:
            if not count.value == 4:
                q = get_command()
                if count.value == 2:
                    speak_up("How can I serve you")
            else:
                speak_up("Im gonna sleep")
                break
            if not q:
                count()
                continue    
            else:
                count.reset()    
            print(f"Query: {q}")
            response_from_agent = await agent.run(q)
            print(f"Agent Response: {response_from_agent.output}")
            speak_up(response_from_agent.output)


if __name__ == '__main__':
    # initial setup
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    print("Voice Assistant is active\n\n")
    speak_up(f"Hello My Dear Friend, How Can I Help You")
    greetings()
    asyncio.run(main())