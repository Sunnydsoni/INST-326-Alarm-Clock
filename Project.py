# INST-326-Alarm-Clock
Final Project

import datetime
import time
import webbrowser
import os


def dateEntry():
    inDay = input("Enter the desired date for alarm (mm/dd/yyyy): ").split("/")

    try:
        inDay = [int(x) for x in inDay]
        valid = True
    except ValueError:
        valid = False

    while not valid or len(inDay) != 3:

        print("Date is not in correct format.")

        inDay = input("Enter the desired date for alarm (mm/dd/yyyy): ").split("/")

        try:
            inDay = [int(x) for x in inDay]
            valid = True
        except ValueError:
            valid = False

    return inDay

def timeEntry():
    inTime = input("Enter the desired time for alarm (hh:mm:ss): ").split(":")

    try:
        inTime = [int(x) for x in inTime]
        valid = True
    except ValueError:
        valid = False

    while not valid or len(inTime) != 3:

        print("Date is not in correct format.")

        inTime = input("Enter the desired time for alarm (hh:mm:ss): ").split(":")

        try:
            inTime = [int(x) for x in inTime]
            valid = True
        except ValueError:
            valid = False

    return inTime

def cls():
    os.system('cls')

inDate = datetime.datetime(1900, 1, 1, 0, 0, 0, 0)

nowDate = datetime.datetime.now()
nowDate = nowDate.replace(microsecond=0)

finalDay = dateEntry()
finalTime = timeEntry()

inDate = inDate.replace(year=finalDay[2])
inDate = inDate.replace(month=finalDay[0])
inDate = inDate.replace(day=finalDay[1])
inDate = inDate.replace(hour=finalTime[0])
inDate = inDate.replace(minute=finalTime[1])
inDate = inDate.replace(second=finalTime[2])

while inDate < datetime.datetime.now():
    print("This time is before now, enter another time.")

    finalDay = dateEntry()
    finalTime = timeEntry()

    inDate = inDate.replace(year=finalDay[2])
    inDate = inDate.replace(month=finalDay[0])
    inDate = inDate.replace(day=finalDay[1])
    inDate = inDate.replace(hour=finalTime[0])
    inDate = inDate.replace(minute=finalTime[1])
    inDate = inDate.replace(second=finalTime[2])

nowDate = datetime.datetime.now()
nowDate = nowDate.replace(microsecond=0)

url = input("Enter a url to open at alarm, or random for a random song from a genre of your choosing: ")

while nowDate != inDate:

    nowDate = datetime.datetime.now()
    nowDate = nowDate.replace(microsecond=0)
    cls()
    print("Time: " + str(nowDate))
    print("Alarm: " + str(inDate))
    time.sleep(1)

print("-----------------------")
print("Alarm Reached")
print("-----------------------")

if url.lower() == "random":
    #get desired genre and find video
    genre = input("Which genre would you like?")
    
else:
    webbrowser.open(url, new=0, autoraise=True)
