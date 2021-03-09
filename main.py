import random #import random library
import pyttsx3 #import pyttsx3 library
import datetime #import datetime library


engine = pyttsx3.init() #engine talking
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # voice id [1] for female, [0] for male voice
engine.runAndWait()


#create list: user possibils saying to bots.
hellow = ["hi","hello", "is anyone there", "good day", "hello there"]

thank = ["thanks", "thank you", "thanks dear", "thank you very much", "thank you soo much", "thanks bots", "thanks bot"]

ofcTime = ["tell me the office time?", "tell me office time?","office time?","what time of office?"]

breakTime = ["tell me the break time?", "tell me break time?","break time?","what time of break?"]

crntTime = ["current time", "time now", "time", "today time"]

owner = ["owner of digitap", "owner of earth organic", "owner of pakoneshop", "founder of digitap",
         "founder of earth organic", "founder of pakoneshop","ceo of digitap", "ceo of earth organic",
         "ceo of pakoneshop", "owner digitap", "owner earth organic", "owner pakoneshop", "founder digitap",
         "founder earth organic", "founder pakoneshop","ceo digitap", "ceo earth organic", "ceo pakoneshop"]

address = ["office address", "address of digitap", "address of office"]

ofcAppTeam = ["team of digitap", "digitap team", "team digitap", "mobile app team" , "app team"]

teamNasir = ["who is nasir", "nasir?", "about nasir"]

teamHasan = ["who is hasan", "hasan?", "about hasan"]

ofcGraphicTeam = ["team of pakone shop", "pakoneshop team", "team pakoneshop", "marketing team" , "advertising team", "creation team"]
# List End...


#create loop for continue program works.
while True:
    a = input("User Said...") #get input from user
    if a.lower() in hellow: # condition and convert command into lower case
        botans = ["Hello !", "Hi", "Hi There", "Welcome"] #bots get answer in this list for user
        print('Bots Said - '+random.choice(botans)+'\n') #bots generate random answer on screen

    elif a.lower() in thank: # condition and convert command into lower case
        print('Bots Said - | Your Welcome |' '\n')  # bots print team directory on screen
        engine.say('| Your Welcome |') #bot's Talking
        engine.runAndWait()

    elif a.lower() in crntTime:
        time = datetime.datetime.now().strftime('%H:%M:%S')
        print(time)
        engine.say(time)
        engine.runAndWait()


    elif a.lower() in ofcTime: # condition and convert command into lower case
        botans = ["( 10:00 AM ) Office Time", "( 10:00 AM - 06:00 PM ) Office Time", "( 10:00 - 18:00 ) Office Time"] #bots get answer in this list for user
        print('Bots Said - '+random.choice(botans)+'\n') #bots generate random answer on screen

    elif a.lower() in breakTime: # condition and convert command into lower case
        botans = ["( 01:00 PM - 02:00 PM ) Break Time", "( 13:00 - 14:00 ) Break Time"] #bots get answer in this list for user
        print('Bots Said - '+random.choice(botans)+'\n') #bots generate random answer on screen

    elif a.lower() in owner: # condition and convert command into lower case
        print('Bots Said - | Mr. Muddasir Hafeez |' '\n')  # bots print team directory on screen
        engine.say('| Mr. Muddasir Hafeez |')
        engine.runAndWait()

    elif a.lower() in address: # condition and convert command into lower case
        print('Bots Said - | Opposite CCA Club, Main Shahrah-e-Faisal, Karachi. 75270 |' '\n')  # bots print team directory on screen
        engine.say('|Office address: A-17, Ground Floor, Opposite CCA Club, Main Shahrah-e-Faisal, Karachi. 75270 |')
        engine.runAndWait()

    elif a.lower() in ofcAppTeam: # condition and convert command into lower case
        print('Bots Said - | Nasir Hussain | Hassan | Muhammad Hammad | Ajay Shamker | Luksh |' '\n') #bots print team directory on screen
        engine.say('| Nasir Hussain , Hassan , Muhammad Hammad , Ajay Shamker , Luksh |')
        engine.runAndWait()

    elif a.lower() in teamNasir: # condition and convert command into lower case
        print('Bots Said - | Nasir Hussain Junior Software Engineer at Digitap Business Solution pvt ltd. |' '\n') #bots print team directory on screen
        engine.say('| Nasir Hussain Junior Software Engineer at Digitap Business Solution pvt ltd. |')
        engine.runAndWait()

    elif a.lower() in teamHasan: # condition and convert command into lower case
        print('Bots Said - | Hasan Haroon Senior Mobile App Developer at Digitap Business Solution pvt ltd. |' '\n') #bots print team directory on screen
        engine.say('| Hasan Haroon Senior Mobile App Developer at Digitap Business Solution pvt ltd. |')
        engine.runAndWait()

    elif a.lower() in ofcGraphicTeam: # condition and convert command into lower case
        print('Bots Said - | Saad Meer | Muhammad Umer | Muhammad Uzair | Hammad Niazi |' '\n') #bots print team directory on screen


#program continue working Until press stop key of the editor.
