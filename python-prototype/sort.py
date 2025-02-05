import pyttsx3
import passes
import json
import re

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def reply(content):
    jsondata = passes.pass1(content=content)
    printdata = re.search(r'{.*}', jsondata, re.DOTALL).group(0)
    data = json.loads(printdata)
    print(data["personal_info"],"\n",data["time_range"],"\n")
    #access time range data here
    with open("info.txt", "a") as file:
        file.write((" " + str(data["personal_info"]))) 
    with open("info.txt", "r") as file:
        context = file.read()
    finaljson = passes.pass2(content=content,context=context,timecontext="")
    finaldata = re.search(r'{.*}', finaljson, re.DOTALL).group(0)
    print(finaldata)
    final = json.loads(finaldata)
    return final

'''
    # Parse the string as JSON
    ret_data = json.loads(ret)

    # Extract the 'feedback' field
    feedback_text = ret_data.get('feedback', '')

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional, you can customize)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

    # Use text-to-speech
    engine.say(feedback_text)
    engine.runAndWait()
'''
'''
prompt1 = "i usually sleep from 3AM to 8PM, and I have to work for my job from 9AM to 6PM, i work in an insurance firm and my interests are playing guitar and hanging out with my girlfriend, i also like playing football"
prompt2 = "hey vector, its been a long week, oh thursday. so let's see, what all do i have going on right now, i gave my laundry, i should collect it before 9 tonight, uhm, i need to get printouts for my rdbms lab tomorrow, ill uhh collect it this evening, i'll study uhh statistics saturday afternoon and uhh go for my keyboard auditions saturday evening also, remind me to shoot a message to lila for dinner, but its not like i can keep her off my mind"
print(passes.startpromp(prompt1),"\n")
reply(prompt2)
'''