import time
from datetime import datetime, timedelta

time_ended=datetime.now()

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))


input("\nPress Enter to start\n\n")
start_time = time.time()

input("Press Enter to stop")
end_time = time.time()

time_lapsed = end_time - start_time
time_started=timedelta(((time_lapsed/24)/60)/60)

print("\nTime started: ",time_ended-time_started)
time_convert(time_lapsed)
print("Time finished: ",time_ended,"\n")