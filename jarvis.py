import openai
import pyttsx3
import speech_recognition as sr


openai.api_key = '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'

engine = pyttsx3.init()

r = sr.Recognizer()
mic = sr.Microphone(device_index=2)
print(sr.Microphone.list_microphone_names())

conversation = ""
user_name = "alex"

while True:
    with mic as source:
        print('listening')
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
    print("no longer listening...")

    try:
        user_input = r.recognize_google(audio)
        print("user input :" + user_input)
    except Exception as e:
        print(e)
        continue

    prompt = user_name + ": " + user_input + "\Jarvis:"
    conversation += prompt

    response = openai.Completion.create(engine='text-davinci-003', prompt=conversation, max_tokens=200)
    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split(user_name + ": ", 1)[0].split("Jarvis: " + ": ", 1)[0]
    
    conversation += response_str + "\n"
    print(response_str)
    
    engine.say(response_str)
    engine.runAndWait()
