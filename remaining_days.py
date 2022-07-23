from datetime import date, datetime, timedelta

now = datetime.now()

print("Write date in order to calculate how many days are until that time")

get_day=int(input("Day: "))

n_days = timedelta(days=get_day)
new_date=now+n_days

print('Today is:            ', now)
print('New date is on:      ', new_date)
print('Days until New Date: ', n_days)