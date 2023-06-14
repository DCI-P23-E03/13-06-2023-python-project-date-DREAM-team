import datetime as dt
import time as tm
import calendar as cl
from dateutil.relativedelta import relativedelta
import pytz


# crstns was here


user_input = input("")

now = dt.datetime.now()

print("Todays date and time: ", now)


unix_time = tm.time()

print("Unix time: ", unix_time)

date_string = "2023-05-03"

converted_date = dt.datetime.strptime(date_string, "%Y-%m-%d")
print("Date: ", converted_date)
print("Type of converted_date: ", type(converted_date))



if cl.isleap(2023) == True:
    print("2023 is a leap year")
else:
    print("2023 is not a leap year")

print("Lets just check if the next year is a leap year:")
if cl.isleap(2024) == True:
    print("2024 is a leap year")
else:
    print("2024 is not a leap year")

next_leap_year_str = "2024-01-01 00:00:01" # the first second of the next leap year

converted_next_leap_year_str = dt.datetime.strptime(next_leap_year_str, "%Y-%m-%d %H:%M:%S")

print(f"Time remaining until the next leap year: {converted_next_leap_year_str - now} hours. ")




#print(type(converted_next_leap_year_str))

#print(type(dt.datetime.now()))

deltatime = relativedelta(now, converted_next_leap_year_str)
print(f"Time until next leap year: {deltatime.years} years, {deltatime.months} months, {deltatime.days} days, {deltatime.hours} hours, {deltatime.minutes} minutes, {deltatime.seconds} seconds")

print(cl.month(2023, 6))



choose_timezone = input("""
Choose a timezone: 
1. Tokyo/Japan
2. Dublin/Ireland
3. San Francisco/USA
4. Berlin/Germany
5. Johannesburg/South Africa
(enter 1, 2, 3, 4 or 5)
""")



if choose_timezone == "1":
    print("Current time in Tokyo: ", dt.datetime.now(pytz.timezone('Asia/Tokyo')).strftime('%Y-%m-%d %H:%M:%S'))
elif choose_timezone == "2":
    print("Current time in Dublin: ", dt.datetime.now(pytz.timezone('Europe/Dublin')).strftime('%Y-%m-%d %H:%M:%S'))
elif choose_timezone == "3":
    print("Current time in San Francisco: ", dt.datetime.now(pytz.timezone('US/Pacific')).strftime('%Y-%m-%d %H:%M:%S'))
elif choose_timezone == "4":
    print("Current time in Berlin: ", dt.datetime.now(pytz.timezone('Europe/Berlin')).strftime('%Y-%m-%d %H:%M:%S'))
elif choose_timezone == "5":
    print("Current time in Johannesburg: ", dt.datetime.now(pytz.timezone('Africa/Johannesburg')).strftime('%Y-%m-%d %H:%M:%S'))



time_in_Sydney = dt.datetime.now(pytz.timezone('Australia/Sydney')).strftime('%Y-%m-%d %H:%M:%S')

time_in_Berlin = ("Current time in Berlin: ", dt.datetime.now(pytz.timezone('Europe/Berlin')).strftime('%Y-%m-%d %H:%M:%S'))
print("Time in Sydney: ", time_in_Sydney)
print("Time in Berlin: ", time_in_Berlin)
print("Difference between Berlin and Sydney: ")

