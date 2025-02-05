import google.generativeai as genai
genai.configure(api_key="TERIMAKIKEY")
model = genai.GenerativeModel('gemini-1.5-flash')
import json

def pass1(content):
    prompt = (
        f"Here is some content: \"{content}\". "
        "You will be given a certain amount of text by the user, where the user is talking about their meetings for the following days or the same day, you are required to extract the following info, and return it strictly in json format."
        "1. Any personal information that can be extracted from the user, is the shortest amount of characters possible, for example: has gilfriend, works at xyz company/tech job/insurace, goes to gym, plays guitar, put more emphasis on activities where the user might have frequent commitments"
        "2. the entire time range of things was the user is talking about, so if the user wants to set calender dates between 6:00 to 16:00, return 6:00 to 14:00, remember that the user might not speak in 24 hour format so you will have to do that conversion yourself, return \"start_time\" and \"end_time\""
        "also if the user is undecided what what times to set certain tasks but gives a rough range (for example, before 9 at night, or after 4 in the morning), factor that in the range aswell"
        "remember to strictly return in json format with \"personal_info\" and \"time_range\", and nothing else, don't add a header or footer before or after the brackets"
    )
    response = model.generate_content(prompt)
    ret = response.text.strip()
    return ret

def pass2(content,context,timecontext):
    prompt = (
        f"Here is some content: \"{content}\". "
        "You are given a certain amount of text by the user above, where the user is talking about their meetings for the following days or the same day, you are also given user context below this line, which gives info about the users current calendar inputs"
        f"\"{context}\""
        "now below this line your are given information about the users current tasks"
        f"\"{timecontext}\""
        "your job is to give the following data in json format, feel free to use nested json for task 1 and 2"
        "1. write in json format, the tasks the user wants to do, only set this if the user has specified at what time the task needs to be done, with title and time range in each, until specified set default time range as 1 hour, give the headers as \"title\", \"start_time\" and \"end_time\", ONLY USE THIS FIELD WHEN USER HAS SPECIFIED THE START TIME"
        "only add tasks in task 1 if the user has specified the start time"
        "don't add tasks if user doesn't specify start times"
        "2. if the user has a task to do but hasnt specified what at what time, smartly analyze the time context if given about the users current tasks and also keep in mind convential human sleep schedules and daily schedules, and decide suitable times and return in a json format, give the headers as \"title\", \"start_time\" and \"end_time\""
        "remember to adhere to conventional human schedules, like breakfast in the morning around 9:00, lunch in the afternoon around 13:00 and dinner at night around 21:00"
        "3. if required, give the user some polite advice on if they are overworking or if they need a break, only when necessary, utilize personalized context if needed"
        "make sure all 3 are in one json file, if required you can nest the jsons for task 1 and 2, but keep them seperate"
        "remember to strictly return in json format, and nothing else, don't add a header or footer before or after the brackets, NOTHING BEFORE OR AFTER THE FIRST AND LAST BRACKETS PLEASE DONT ADD THOSE BACKTICKS AND THINGS"
        "remember stick to json and not add any text or symbols before and after the final brackets"
    )
    response = model.generate_content(prompt)
    ret = response.text.strip()
    return ret

def startpromp(content):
    prompt = (
        f"Here is some content: \"{content}\". "
        "A user has been prompted on creating an account to describe their day and their activities, like what time they sleep and what are some daily commitments they have to commit to"
        "your job is to return the following 2 things in json format"
        "1. if the user identifies any commitments with specific timings, return it in json format, with the following headers: activity, start_time and end_time"
        "2. if the user speaks about any commitments without any time commitments, or gives information about their current life, put it in very concise terms, for example: works in insurace, has a girlfriend, plays guitar, etc."
        "remember to return both of these in one json but seperated, feel free to implement nested jsons for the first point, for the second put everything in one string, keep the title for the second one as \"info\", also dont add any headers or footers before or after the json"
        "remember to strictly adhere to json format without adding headers or footers before or after the brackets, NOTHING BEFORE OR AFTER THE FIRST AND LAST BRACKETS"
    )
    response = model.generate_content(prompt)
    ret = response.text.strip()
    jsondata = json.loads(ret)
    with open("info.txt", "a") as file:
        file.write(jsondata["info"]) 
    return ret