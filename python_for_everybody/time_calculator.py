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






from time import time


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
    start_s = []
    duration_d = []
    start_part_day = ''
    day_of_week_str = str.lower(day_of_week)
    am = None
    pm = None
    ampm_minutes = None
    new_day_week = ''
    days_later = ''

    for a, b in zip(start, duration):
        # print(a, b)
        start_s += a # puts start into string format
        duration_d += b # puts duration in string format

    for a in start:
        #print(a)
        start_part_day += a
    ampm = start_part_day[-2] + start_part_day[-1] # We extract if it's am or pm
    new_start = start[0:5]
    new_duration = duration[0:5]
    #print(new_start)
    new_start_strip = new_start.rstrip()
    #print(new_start_strip)
    #print(new_duration)
    new_duration_strip = new_duration.rstrip()
    #print(new_duration_strip)
    if len(new_duration_strip) < 5:
        new_duration_strip = '0' + new_duration_strip
    if len(new_start_strip) < 5:
        new_start_strip = '0' + new_start_strip


    
    
    print(ampm)
    print(new_start_strip)
    print(new_duration_strip)
    print(day_of_week_str)
    nss_h_int = int(new_start_strip[0:2]) # starting hour
    nss_m_int = int(new_start_strip[3:5])
    nds_h_int = int(new_duration_strip[0:2])
    nds_m_int = int(new_duration_strip[3:5])
    duration_time = (nds_h_int * 60) + nds_m_int
    
    if ampm == 'AM':
        am = True
        start_time = (nss_h_int * 60) + nss_m_int

    if ampm == 'PM':
        start_time = 719 + (nss_h_int * 60) + nss_m_int
        pm = True

    print(str(start_time))
    print(str(duration_time))
    
    nt_calc = start_time + duration_time
    print(str(nt_calc)) # This gives me the total minutes from start time to duration when not given a specific week day to start on

    If nt_calc <= 1439:
        new_day_week = 'Sunday'
    elif nt_calc >= 1440 and <= 2879:
         new_day_week = 'Monday'
    elif nt_calc >= 2880 and <= 4319:
         new_day_week = 'Tuesday'
    elif nt_calc >= 4320 and <= 5759:
         new_day_week = 'Wednesday'
    elif nt_calc >= 5760 and <= 7199:
         new_day_week = 'Thursday'
    elif nt_calc >= 7200 and <= 8639:
         new_day_week = 'Friday'
    elif nt_calc >= 8640 and <= 10079:
         new_day_week = 'Saturday'
    elif nt_calc >= 10080:
        days_later_num = (10080/60)
        






print(add_time("2:59 AM", "24:00", "saturDay"))