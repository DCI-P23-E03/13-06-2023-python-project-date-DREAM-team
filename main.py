import datetime as dt
import time as tm
import calendar as cl
from dateutil.relativedelta import relativedelta
import pytz
import random



user_input = input("""Enter a number to choose an option:
                   1. Display the current date and time
                   2. Display the current Unix epoch time
                   3. Show the convertion of a string to a datetime object
                   4. Leap year calculator   
                   5. Show calender of current month
                   6. Timezone converter
                   7. Show time of the other side of the world
                   8. Tell a joke
                   9. Surprise me
                   """)

now = dt.datetime.now()

if user_input == "1":
    print("Todays date and time: ", now)
elif user_input == "2":
    unix_time = tm.time()
    print("Unix time: ", unix_time)
elif user_input == "3":
    date_string = "2023-05-03"
    converted_date = dt.datetime.strptime(date_string, "%Y-%m-%d")
    print("Date: ", converted_date)
    print("Type of converted_date: ", type(converted_date))
elif user_input == "4":
    if cl.isleap(2023) == True:
        print("2023 is a leap year")
    else:
        print("2023 is not a leap year")
    tm.sleep(3)
    print("Lets just check if the next year is a leap year:")
    if cl.isleap(2024) == True:
        print("2024 is a leap year")
    else:
        print("2024 is not a leap year")

    next_leap_year_str = "2024-01-01 00:00:01" # the first second of the next leap year
    converted_next_leap_year_str = dt.datetime.strptime(next_leap_year_str, "%Y-%m-%d %H:%M:%S")
    print(f"Time remaining until the next leap year: {converted_next_leap_year_str - now} hours. ")

    deltatime = relativedelta(now, converted_next_leap_year_str)
    print(f"Time until next leap year: {deltatime.years} years, {deltatime.months} months, {deltatime.days} days, {deltatime.hours} hours, {deltatime.minutes} minutes, {deltatime.seconds} seconds")
elif user_input == "5":
    print(cl.month(2023, 6))
elif user_input == "6":

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

elif user_input == "7":

    time_in_Sydney = dt.datetime.now(pytz.timezone('Australia/Sydney')).strftime('%Y-%m-%d %H:%M:%S')

    time_in_Berlin = ("Current time in Berlin: ", dt.datetime.now(pytz.timezone('Europe/Berlin')).strftime('%Y-%m-%d %H:%M:%S'))
    print("Time in Sydney: ", time_in_Sydney)
    print("Time in Berlin: ", time_in_Berlin)
    print("Difference between Berlin and Sydney: 8 hours")

elif user_input == "8":
    print("Get ready to laugh")
    tm.sleep(3)

    random_number = random.randint(1, 4)
    if random_number == 1:
        print("Why do programmers prefer dark mode?")
        tm.sleep(3)
        print("Because light attracts bugs!")
    elif random_number == 2:
        print("Why did the programmer quit his job?")
        tm.sleep(3)
        print("Because he didn't get arrays!")
    elif random_number == 3:
        print("Why does Python live on Land?")
        tm.sleep(3)
        print("Because it is above C level!""")
    else:
        print("Why don't programmers like nature?")
        tm.sleep(3)
        print("It has too many bugs!")

elif user_input == "9":
    def endless_progress_bar():
        print("Ready for a surprise?")
       # print("Press any key to stop the progress.")
        while True:
            for symbol in ['-', '\\', '|', '/']:
                print(f'\rLoading: {symbol,symbol,symbol}', end='', flush=True)
                tm.sleep(0.1)

    endless_progress_bar()

else:
    print("Invalid input. Please try again.")
    