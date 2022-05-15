from Speak import Say
import datetime
import cv2
import psutil

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Say("Good Morning!")

    elif hour>=12 and hour<18:
        Say("Good Afternoon!")   

    else:
        Say("Good Evening!")
    Say("Hello sir i am jarvis how may i help you")

def Time():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    print(strTime)
    Say(f"Sir the time is {strTime}")

def Date():
    strdate = datetime.date.today()
    print(strdate)
    Say(f"Sir today's date is {strdate}")

def speedtest(query):
    import speedtest
    Say("ok sir, wait a minute i am checking the internet speed")     
    sp = speedtest.Speedtest()
    down = sp.download()
    correctDown = int(down/800000)
    up = sp.upload()
    correctUp = int(up/800000)

    if"uploading" in query:
        Say(f"the uploading speed is {correctUp} mbp s")
    elif"downloading" in query:
        Say(f"the downloading speed is {correctDown} mbp s")  
    else:
        Say(f"the uploading speed is {correctUp} mbp s and the downloading speed is {correctDown} mbp s") 

def power():
    battery = psutil.sensors_battery()
    per = battery.percent
    Say(f"sir our system have {per} percentage power") 
    if per>=75:
        Say("sie we have enough power you can continue our work")
    elif per>=45 and per<75:
        Say("sir i think we should connect our system to charging point to charge battery")
    elif per>=15 and per<45:
        Say("sir dont't have enough power to work, please connect to charging")
    elif per<15:
        Say("sir we have very low power, please connect system to charging the system very soon")


def NonInputExecution(query):

    query = str(query)

    if "time" in query:
        Time()
    
    elif "date" in query:
        Date()
    
    elif"speed" in query:
        speedtest(query)
    
    elif"power" in query or "battery" in query:
        power()

