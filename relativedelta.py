
#this simple program will calculate the number of days passed since a given date

import datetime
from dateutil.relativedelta import relativedelta

now = datetime.date.today()

print("enter a start counting date. ")

d = int(input("please enter a day: "))
m = int(input("please enter a month: "))
y = int(input("please enter a year: "))
then = datetime.date(y, m, d)

print("your date was: ",then)
print("today is: ",now)

delta_days = now - then

rdelta = relativedelta(now, then)
print('years passed since: ', rdelta.years)
print('months passed since: ', rdelta.months)
print('days passed since: ', rdelta.days)

print(f"""Since your date passed: 
    {rdelta.years} years
    {rdelta.months} months
    {rdelta.days} days 
        or
    {delta_days} days """)