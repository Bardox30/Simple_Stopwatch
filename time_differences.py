from datetime import date, datetime

now = datetime.now()

print("Write date in order to calculate how many days are until that time")

get_day=int(input("Day: "))
get_month=int(input("Month: "))
get_year=int(input("Year: "))

new_date = datetime(day=get_day, month=get_month, year=get_year)
countdown = new_date - now

print('Today is: ', now)
print('New Year is on: ', new_date)
print('Days until New Years: ', countdown.days)