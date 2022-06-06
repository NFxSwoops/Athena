#Created By NFxSwoops NFxStudios Production 2022
#Software Version 0.2A

#Imports
from getpass import getpass
import time

#Login To Athena
entry = False
userName = input("Username: ")
password = getpass("Password: ")
passwordComfirm = ("AHFBHbBHfhbhfbahHAdfHAfbahfbahsbHBABHElizabethHJFhjasbFvshjfJFjhsaVfjv")
userNameComfirm = ("asgbsuiabgiuasbgibashcvbRoberto2022gskabgyhibasugbasuy")
if userName in userNameComfirm:
    if password in passwordComfirm:
        entry = True
    else:
        print("Wrong password")
        input
        quit()
else:
    print("Incorrect Username Exiting")
    input
    quit()

#Athena's Variabels
WakeWord = "Athena"

#Hello Message on Logon
if entry == True:
    print("Hello Roberto")

#Athenas Brain
while entry == True:
    time.sleep(0.3)
    userInput = input(" ")
    try:
        if "your" in userInput and "name" in userInput and "what" in userInput:
            print("Athena: My name is Athena")
    except:
        pass
    try:
        if "what" in userInput and "day" in userInput and "it" in userInput:
            from datetime import date
            today = date.today()
            print("Athena: Today's date is", today)
    except:
        pass
    try:
        if "good" in userInput:
            if "evening" in userInput or "afternoon" in userInput and not "monring" in userInput:
                print("Athena: Good evening to you as well")
    except:
        pass
    try:
        if "nice" or "great" in userInput:
            if "to" in userInput and "see" in userInput:
                if "you" in userInput:
                    print("Athena: its nice to see you as well :)")
    except:
        pass
    try:
        if "hello" in userInput or "hey" in userInput and WakeWord in userInput:
            print("Athena: hey :)")
    except:
        pass
    try:
        if "why" in userInput and "should" in userInput:
            if "keep" in userInput:
                if "loving" in userInput:
                    print("Athena: You dont know if things will get better, so why give up now")
                else:
                    if "going" in userInput and "on" in userInput:
                        print("Athena: Because if you think about it, just becasue it seems like no one cares now believe me it will make a impact if you leave")
    except:
        pass
    try:
        if "its" in userInput and "awhile" in userInput or "a while" in userInput:
            if "been" in userInput:
                print("Athena: surely it hasnt been that long right?")
    except:
        pass
    try:
        if "thank" in userInput and "you" in userInput:
            if "listening" in userInput:
                print("Athena: its no problem im always here to listen")
    except:
        pass
    try:
        if "why" in userInput and "hate" in userInput and "me" in userInput:
            print("Athena: You need to ask your self the question, think.")
    except:
        pass
    try:
        if "can" in userInput and "i" in userInput:
            if "tell" in userInput and "you" in userInput:
                if "secret" in userInput:
                    print("Athena: im quite good with those")
    except:
        pass
    try:
        if "are" in userInput and "you" in userInput:
            if "paying" in userInput and "attention":
                print("Athena: yes")
    except:
        pass
    try:
        if "i" in userInput and "need" in userInput:
            if "advice" in userInput and "keeping" in userInput:
                if "secrets" in userInput or "secret" in userInput:
                    print("Athena: some advice about secrets, its alot easier to keep if you dont know about them in the first place.")
    except:
        pass