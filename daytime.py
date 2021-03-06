
from datetime import datetime

now = datetime.now() # current date and time

newDateNow=datetime.now()
newDatePast=datetime(2020,3,15)
time_passed=newDateNow-newDatePast

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)
print("From day: ",newDatePast)
print("To: ",newDateNow)
print("Has passed: ",time_passed)