# INST-326-Alarm-Clock
Final Project

import datetime
import time
import webbrowser
import os
import random


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

#Prompts user for what time they want the alarm to go off. Exception handling included for an entry in an incorrect format
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
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Function that takes in the users genre input, then selects a random YouTube video from the specified list. Code by Baldwin          
def song(genre):
    country = ["https://www.youtube.com/watch?v=Ct9BFr9XBaI", "https://www.youtube.com/watch?v=p_IwENcMPOA",
               "https://www.youtube.com/watch?v=dRX0wDNK6S4", "https://www.youtube.com/watch?v=nADTbWQof7Y"]
    rap = ["https://www.youtube.com/watch?v=VSXJkvQOLP0", "https://www.youtube.com/watch?v=oCveByMXd_0",
               "https://www.youtube.com/watch?v=8fbyfDbi-MI"]
    rock = ["https://www.youtube.com/watch?v=ROatPGGMvXg", "https://www.youtube.com/watch?v=8SbUC-UaAxE",
            "https://www.youtube.com/watch?v=u9Dg-g7t2l4"]
    pop = ["https://www.youtube.com/watch?v=nfWlot6h_JM",
           "https://www.youtube.com/watch?v=ffxKSjUwKdU&list=PLMC9KNkIncKvYin_USF1qoJQnIyMAfRxl",
           "https://www.youtube.com/watch?v=lp-EO5I60KA&list=PLMC9KNkIncKvYin_USF1qoJQnIyMAfRxl&index=1"]

    if genre == 1:
        return random.choice(country)
    elif genre == 2:
        return random.choice(rap)
    elif genre == 3:
        return random.choice(rock)
    elif genre == 4:
        return random.choice(pop)




inDate = datetime.datetime(1900, 1, 1, 0, 0, 0, 0)

nowDate = datetime.datetime.now()
nowDate = nowDate.replace(microsecond=0)

url = input("Enter a url to open at alarm, or random for a random song from a genre of your choosing: ")

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
    # get desired genre and find video
    genre = input("Which genre would you like? Enter a number. 1) Country 2) Rap 3) Rock 4) Pop: ")
    url = song(int(genre))
    webbrowser.open(url, new=0, autoraise=True)
else:
    webbrowser.open(url, new=0, autoraise=True)
   
