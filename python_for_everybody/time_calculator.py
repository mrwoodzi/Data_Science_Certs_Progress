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
    ampm_minutes = None
    new_day_week = ''
    days_later = None
    minutes_in_week = None

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
        ampm_minutes = (nss_h_int * 60) + nss_m_int
    elif ampm == 'PM':
        ampm_minutes = 719 + (nss_h_int * 60) + nss_m_int
        pm = True
    else ampm == None:

    #print(str(start_time))
    #print(str(duration_time))

    if day_of_week == True:
        if day_of_week_str_lower <= 1439:
            new_day_week = 'sunday'
            minutes_in_week = ampm_minutes 
        elif day_of_week_str_lowe >= 1440 <= 2879:
            new_day_week = 'monday'
            minutes_in_week = 1440 + ampm_minutes 
        elif day_of_week_str_lowe >= 2880 <= 4319:
            new_day_week = 'tuesday'
            minutes_in_week = 2880 + ampm_minutes 
        elif day_of_week_str_lowe >= 4320<= 5759:
             new_day_week = 'wednesday'
            minutes_in_week = 4320 + ampm_minutes 
        elif day_of_week_str_lowe >= 5760 <= 7199:
            new_day_week = 'thursday'
            minutes_in_week = 5760 + ampm_minutes
        elif day_of_week_str_lowe >= 7200<= 8639:
             new_day_week = 'friday'
            minutes_in_week = 7200 + ampm_minutes
        elif day_of_week_str_lowe >= 8640 <= 10079:
            new_day_week = 'saturday'
            minutes_in_week = 8640 + ampm_minutes

    
    
    nt_calc = ampm_minutes + duration_time
    #print(str(nt_calc)) # This gives me the total minutes from start time to duration when not given a specific week day to start on

    if duration_time >= 10080:
        days_later_num = ((nt_calc/60)/24) #gives me number of days later
        #print(str(days_later_num))
        dlns_r = round(days_later_num, 2) #rounds the float from days_later_num
        #print(dlns_r)
        dlns_rs = str(dlns_r)
        days_later, b = map(int,dlns_rs.split(".", 1)) #splits float into days and percentage of a day
        #print(days_later, b) # checking that I split the float
        days_later_str = str(a)
        new_time_day = round((int(b)*.01)*24, 2) # turning b back into decimal and figuring what time of the new day it is
        #print(new_time_day)
        while nt_calc > 10080: # this brings the orginal nt_calc down to a real number so we can figure out what day of the week it is
            nt_calc = nt_calc - 10080

    if nt_calc <= 1439:
        new_day_week = 'Sunday'
    elif nt_calc >= 1440 <= 2879:
         new_day_week = 'Monday'
    elif nt_calc >= 2880<= 4319:
         new_day_week = 'Tuesday'
    elif nt_calc >= 4320<= 5759:
         new_day_week = 'Wednesday'
    elif nt_calc >= 5760 <= 7199:
         new_day_week = 'Thursday'
    elif nt_calc >= 7200<= 8639:
         new_day_week = 'Friday'
    elif nt_calc >= 8640 <= 10079:
         new_day_week = 'Saturday'
   



    
    #elif day_of_week != True and days_later > 2:
    #    return(f'{new_time_day} {ampm}, ({days_later_str} days later)')
    #elif day_of_week == True and days_later > 2:
    #    return(f'{new_time_day} {ampm}, {new_day_week}, ({days_later_str} days later)')
        






print(add_time("8:16 PM", "466:02", "saturDay"))