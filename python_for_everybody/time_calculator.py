# need 2 required parameters and one optional
# (1, 2, Day_of_Week=None)
#What is the best way for program to know what day of the week it is? Have a total number of total hours in a week
#If the result will be the next day, it should show (next day) after the time.
#If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.
#All needs to be return in a string in " "

#Need to calculate the basic time in a day, week and mulitple days

# add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

# add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

# add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

# add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)






def add_time(start, duration, day_of_week=None):
    # am = 0-719
    # pm = 720-1439
    # Sunday = 0 - 1439, pm starts at 720min 
    # Monday = 1140 - 2879, pm starts at 2160min
    # Tuesday = 2880-4319, pm starts at 3600min
    # Wednesday = 4320-5759, pm starts at 5040min
    # Thursday  = 5760-7199, pm starts at 6480min
    # Friday = 7200-8639, pm starts at 7920min
    # Saturday = 8640-10079, pm starts at 9360
    # time_single_day = 0-1439
    # min = 1
    # hr = 60min
    # day <= 1439
    start_s = '' 
    duration_d = ''
    start_part_day = ''
    day_of_week_str = str.lower(day_of_week)
    am = None
    pm = None
    ampm_minutes = None

    for a, b in zip(start, duration):
        # print(a, b)
        start_s += a # puts start into string format
        duration_d += b # puts duration in string format

    for a in start:
        print(a)
        start_part_day += a
    ampm = start_part_day[-2] + start_part_day[-1] # We extract if it's am or pm


    
    
    print(ampm)
    print(start_s)
    print(duration_d)
    print(day_of_week_str)




print(add_time("2:59 AM", "24:00", "saturDay"))