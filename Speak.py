import pyttsx3


def Say(Text):
    engine  = pyttsx3.init("sapi5")
    rate = engine.getProperty('rate')
    engine.setProperty('rate',170)
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    

    print("    ")
    print(f"A.I : {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("    ")

# Say("Welcome Himanshu") 
