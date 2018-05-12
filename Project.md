# INST-326-Alarm-Clock
Final Project

import datetime
import time

inDate = datetime.datetime(1900, 1, 1, 0, 0, 0, 0)
nowDate = datetime.datetime.now()
nowDate = nowDate.replace(microsecond=0)


inDate = inDate.replace(year=int(input("Enter the full year of the desired alarm in digits: ")))
inDate = inDate.replace(month=int(input("Enter the month of the desired alarm in digits: ")))
inDate = inDate.replace(day=int(input("Enter the day of month of the desired alarm in digits: ")))
inDate = inDate.replace(hour=int(input("Enter the hour of the desired alarm in digits: ")))
inDate = inDate.replace(minute=int(input("Enter the minute of the hour of desired alarm in digits: ")))
inDate = inDate.replace(second=int(input("Enter the second of the minute desired alarm in digits: ")))

while inDate < datetime.datetime.now():
   print("This time is before now, enter another time.")

   inDate = inDate.year = int(input("Enter the full year of the desired alarm in digits: "))
   inDate = inDate.month = int(input("Enter the month of the desired alarm in digits: "))
   inDate = inDate.day = int(input("Enter the day of month of the desired alarm in digits: "))
   inDate = inDate.hour = int(input("Enter the hour of the desired alarm in digits: "))
   inDate = inDate.minute = int(input("Enter the minute of the hour of desired alarm in digits: "))
   inDate = inDate.second = int(input("Enter the second of the minute desired alarm in digits: "))

nowDate = datetime.datetime.now()
nowDate = nowDate.replace(microsecond=0)

while nowDate != inDate:

   nowDate = datetime.datetime.now()
   nowDate = nowDate.replace(microsecond=0)
   print("Time: " + str(nowDate))
   print("Alarm: " + str(inDate))
   time.sleep(1)

print("-----------------------")
print("Alarm Reached")
print("-----------------------")
