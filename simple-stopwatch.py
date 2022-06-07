from cgi import print_arguments
import time
from datetime import datetime, timedelta

current_date=datetime.now()

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))


input("Press Enter to start")
start_time = time.time()

input("Press Enter to stop")
end_time = time.time()

time_lapsed = end_time - start_time
time_started=timedelta(((time_lapsed/24)/60)/60)

print("Time started: ",current_date-time_started)
print(time_convert(time_lapsed))
print("Time finished: ",current_date)