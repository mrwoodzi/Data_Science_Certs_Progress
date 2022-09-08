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
    day_of_week_str_lower = str.lower(day_of_week)
    am = None
    pm = None
    ampm_minutes_old = None
    new_day_week = ''
    days_later = None
    minutes_in_week = None
    new_ampm = ''
    next_day = ''
    new_time = ''

    for a in start:
        #print(a)
        start_s += a
    ampm = start_s[-2] + start_s[-1] # We extract if it's am or pm
    for b in duration:
        #print(b)
        duration_d += b
    #print(ampm)
    #print(start_s)
    #print(duration_d)
    dots = ':'
    fds = str(list(pos for pos, char in enumerate(start_s) if char == dots)) # finds : in start
    fdd = str(list(pos for pos, char in enumerate(duration_d) if char == dots)) # finds : in duration
    #print((fds))
    #print((fdd))
    fds_int = int(fds[1])
    fdd_int = int(fdd[1])
    #print(fds_int)
    #print(fdd_int)
    nss_h_int = int(start_s[0:(fds_int)]) # starting hour
    #print(nss_h_int)
    nss_m_int = int(start_s[fds_int+1:fds_int+3])# starting min
    #print(nss_m_int)
    nds_h_int = int(duration_d[0:(fdd_int)])# duration hour
    print(nds_h_int)
    nds_m_int = int(duration_d[fdd_int+1:fdd_int+3])# duration min
    print(nds_m_int)
    time_single_day_in_minutes = (nds_h_int * 60) + nds_m_int # adds total duration time
    
    if ampm == 'AM':
        am = True
        ampm_minutes_old = (nss_h_int * 60) + nss_m_int
    elif ampm == 'PM':
        ampm_minutes_old = 719 + (nss_h_int * 60) + nss_m_int
        pm = True
    duration_time = (nds_h_int * 60) + nds_m_int
    #print(str(start_time))
    print(str(duration_time))


    if duration_time >= 10080:
        days_later_num = ((duration_time/60)/24) #gives me number of days later
        print(str(days_later_num))
        dlns_r = round(days_later_num, 2) #rounds the float from days_later_num
        print(dlns_r)
        dlns_rs = str(dlns_r)
        days_later, hours_min = map(int,dlns_rs.split(".", 1)) #splits float into days and percentage of a day
        print(days_later, hours_min) # checking that I split the float
        days_later_str = str(days_later)
        print(days_later_str)
        new_time_day = round((int(hours_min)*.01)*24, 2) # turning b back into decimal and figuring what time of the new day it is
        print(new_time_day)
        new_time_day_str = str(new_time_day)
        hours, minutes_deci = map(int,new_time_day_str.split(".", 1))
        print(hours, minutes_deci)
        print(str(minutes_deci))
        minutes_int = round((minutes_deci * .01) * 60)
        new_minutes_day_str = str(minutes_int)
        new_minutes_day_str_len = len(new_minutes_day_str)
        if new_minutes_day_str_len == 1:
            new_minutes_day_str = '0' + new_minutes_day_str
        print(new_minutes_day_str)
        if hours <= 12:
            new_hour_day = hours
            new_hour_day_str = str(hours)
            new_ampm = ' AM'
        elif hours >=13 <= 23:
            new_hour_day = hours - 12
            new_hour_day_str = str(new_hour_day)
            new_ampm = ' PM'
        while duration_time > 10080: # this brings the orginal nt_calc down to a real number so we can figure out what day of the week it is
            print(duration_time)
            duration_time = duration_time - 10080
    print(duration_time)
    print(new_hour_day_str, new_minutes_day_str, new_ampm)

    


    new_time = (f'{new_hour_day_str}{dots}{new_minutes_day_str}{new_ampm}{next_day}')

    
    return new_time
    #    return(f'{new_time_day} {ampm}, {new_day_week}, ({days_later_str} days later)')
    




print(add_time("8:16 PM", "466:02", "saturDay"))