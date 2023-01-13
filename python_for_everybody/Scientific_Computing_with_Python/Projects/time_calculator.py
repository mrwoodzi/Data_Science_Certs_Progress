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
    old_start_time_day = None
    new_day_week = ''
    days_later = None
    new_ampm = ''
    next_day = ''
    new_time = ''
    new_hour_day_str = ''
    new_minutes_day_str = ''
    new_day_week = ''
    dots = ':'
    dot = '.'
    comma = ''
    days_later_num = None
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
    fds = str(list(pos for pos, char in enumerate(start_s) if char == dots)) # finds : in start
    fdd = str(list(pos for pos, char in enumerate(duration_d) if char == dots)) # finds : in duration
    #print((fds))
    #print((fdd))
    fds_int = int(fds[1])
    fdd_int = int(fdd[1])
    #print(fds_int)
    #print(fdd_int)
    nss_h_int = int(start_s[0:(fds_int)]) # starting hour 3
    #print(nss_h_int)
    nss_m_int = int(start_s[fds_int+1:fds_int+3])# starting min 30
    #print(nss_m_int)
    nds_h_int = int(duration_d[0:(fdd_int)])# duration hour 2
    #print(nds_h_int)
    nds_m_int = int(duration_d[fdd_int+1:fdd_int+3])# duration min 12
    #print(nds_m_int)
    
    if ampm == 'AM':
        old_start_time_day = nss_h_int + float(nss_m_int/60) # puts start time hours into minutes
    elif ampm == 'PM':
        old_start_time_day = 12 + nss_h_int + float(nss_m_int/60) # puts start time hours into minutes
        #print(str(old_start_time_day))
    
    duration_time_hours = nds_h_int + (nds_m_int/60) 

    #print(ampm)
    #print(duration_time_hours)
    #print(old_start_time_day)

    #this gives me the total number of days later and gives me the hours of the next day in decimal form
    days_later_num_unsplit = duration_time_hours/24 
    days_later_int_deci_str = str((duration_time_hours + old_start_time_day) / 24)
    #print((days_later_int_deci_str))
    days_later_str, nope = map(int,days_later_int_deci_str.split(".", 1))
    #print(days_later_str)
    days_later_int = int(days_later_str)
    days_later_num_unsplit_str = str(days_later_num_unsplit)
    old_days_later_str, hours_in_day_deci_int = map(int,days_later_num_unsplit_str.split(".", 1))

    #print(str(days_later_num_unsplit))
    #print(old_days_later_str)
    hours_in_day_deci_int_float = days_later_num_unsplit % 1
    #print(hours_in_day_deci_int_float)
    #print(hours_in_day_str)
    old_days_later_int = int(old_days_later_str)
    hours_in_day_later_military_deci_str = str(hours_in_day_deci_int_float)
    hours_in_day_deci_str = str(hours_in_day_deci_int_float)
    hours_in_day_deci_str = (hours_in_day_deci_str[0:6])
    #print(hours_in_day_deci_str)
    #print(hours_in_day_deci_flt)
    new_minutes_day_int = (hours_in_day_deci_int_float*24)

    
    #print(str(new_minutes_day_int))


    # this gives me my minutes and starts the hour process
    hours_later_military_deci = old_start_time_day + new_minutes_day_int
    #print(str(hours_later_military_deci))
    new_minutes_day_military_deci = ((hours_later_military_deci % 1))
    #print(str(new_minutes_day_military_deci)) # minutes in decimal
    new_minutes_day_military = round(new_minutes_day_military_deci * 60)
    new_minutes_day_str = str(new_minutes_day_military)
    #print(new_minutes_day_str)

    #gives me the new hour time
    hours_later_military_deci_str = str(hours_later_military_deci)
    hours_later_military, nothing = map(int,hours_later_military_deci_str.split(".", 1))
    #print(str(hours_later_military))

    len_minutes = len(new_minutes_day_str) # gives me len of minutes
    #print(str(len_minutes))
    #print(str(days_later_int))
    if len_minutes == 1:
        new_minutes_day_str = '0' + new_minutes_day_str
    elif len_minutes == 0:
        new_minutes_day_str = '00'    
    hours_later_military_new_day = hours_later_military
    #print(str(hours_later_military_new_day))



    if days_later_int > 2:
        next_day = (f' ({days_later_str} days later)')
        #print(hours_later_military_new_day)
        if hours_later_military_new_day > 25:
            hours_later_military_new_day = hours_later_military_new_day - 24
        if hours_later_military_new_day == 24:
                new_ampm = ' AM'
        if hours_later_military_new_day == 0:
            hours_later_military_new_day = 12
        if hours_later_military_new_day <=  11:
            if hours_later_military_new_day <= 11:
                new_hour_day = hours_later_military_new_day
                #print(str(new_hour_day))
                new_hour_day_str = str(new_hour_day)
                new_ampm = ' AM'
            elif hours_later_military_new_day >= 12 <= 23:
                #print(hours_later_military)
                new_hour_day = hours_later_military_new_day - 12
                #print(new_hour_day)
                new_hour_day_str = str(new_hour_day)
                new_ampm = ' PM'
    elif days_later_int == 2:
        next_day = ' (2 days later)'
        if hours_later_military_new_day > 25:
            hours_later_military_new_day = hours_later_military_new_day - 24
        #print(str(hours_later_military_new_day))
        if hours_later_military_new_day == 24:
            new_hour_day_str = '12'
            new_ampm = ' AM'
        elif hours_later_military_new_day <=  11:
            if hours_later_military_new_day <= 11:
                new_hour_day = hours_later_military_new_day
                #print(str(new_hour_day))
                new_hour_day_str = str(new_hour_day)
                new_ampm = ' AM'
            elif hours_later_military_new_day >= 12 <= 23:
                #print(hours_later_military)
                new_hour_day = hours_later_military_new_day - 12
                #print(new_hour_day)
                new_hour_day_str = str(new_hour_day)
                new_ampm = ' PM'
    elif days_later_int == 1:
        next_day = ' (next day)'
        if hours_later_military_new_day > 25:
            hours_later_military_new_day = hours_later_military_new_day - 24
        if hours_later_military_new_day > 24:
            hours_later_military_new_day = hours_later_military_new_day - 24
        if hours_later_military_new_day == 24:
            new_hour_day_str = '12'
            new_ampm = ' AM'
        elif hours_later_military_new_day <=  11:
            if hours_later_military_new_day <= 11:
                new_hour_day = hours_later_military_new_day
                #print(str(new_hour_day))
                new_hour_day_str = str(new_hour_day)
                new_ampm = ' AM'
            elif hours_later_military_new_day >= 12 <= 23:
                #print(hours_later_military)
                new_hour_day = hours_later_military_new_day - 12
                #print(new_hour_day)
                new_hour_day_str = str(new_hour_day)
                new_ampm = ' PM'
    elif days_later_int == 0:
        next_day = ''
        if hours_later_military_new_day <= 11:
            new_hour_day = hours_later_military
            #print(str(new_hour_day))
            new_hour_day_str = str(new_hour_day)
            new_ampm = ' AM'
        elif hours_later_military_new_day >= 12 <= 23:
            new_ampm = ' PM'
            if hours_later_military_new_day == 12:
                new_hour_day_str = (hours_later_military_new_day)
            else:
                #print(hours_later_military)
                new_hour_day = hours_later_military_new_day - 12
                #print(new_hour_day)
                new_hour_day_str = str(new_hour_day)
            

    
    if day_of_week:
        comma = ','
        day_of_week_str_lower = str.lower(day_of_week)
        if day_of_week_str_lower == 'sunday':
            day_of_week_int_hrs = 0
        elif day_of_week_str_lower == 'monday':
            day_of_week_int_hrs = 24 
        elif day_of_week_str_lower == 'tuesday':
            day_of_week_int_hrs = 48
        elif day_of_week_str_lower == 'wednesday':
            day_of_week_int_hrs = 72
        elif day_of_week_str_lower == 'thursday':
            day_of_week_int_hrs = 96
        elif day_of_week_str_lower == 'friday':
            day_of_week_int_hrs = 120
        elif day_of_week_str_lower == 'saturday':
            day_of_week_int_hrs = 144
        
        days_later_int_sum = days_later_int * 24
        old_start_time_day_week = (day_of_week_int_hrs) + (days_later_int_sum)

        print(day_of_week_int_hrs)
        print(old_start_time_day_week)
        if old_start_time_day_week > 168:
            while old_start_time_day_week > 168:
                print(str(old_start_time_day_week))
                old_start_time_day_week = old_start_time_day_week - 168
        if old_start_time_day_week < 24 or old_start_time_day_week == 168:
            new_day_week = ' Sunday'
        elif old_start_time_day_week >= 24  and old_start_time_day_week < 48:
            new_day_week = ' Monday'
        elif old_start_time_day_week >= 48  and old_start_time_day_week< 72:
            new_day_week = ' Tuesday'
        elif old_start_time_day_week >= 72  and old_start_time_day_week< 96:
            new_day_week = ' Wednesday'
        elif old_start_time_day_week >= 96 and old_start_time_day_week < 120:
            new_day_week = ' Thursday'
        elif old_start_time_day_week >=  120  and old_start_time_day_week< 144:
            new_day_week = ' Friday'
        elif old_start_time_day_week >= 144 and old_start_time_day_week < 168:
            new_day_week = ' Saturday'


    new_time = (f'{new_hour_day_str}{dots}{new_minutes_day_str}{new_ampm}{comma}{new_day_week}{next_day}')
    
    return new_time
    

    

print(add_time("8:16 PM", "466:02", "tuesday"))
#actual = add_time("8:16 PM", "466:02", "tuesday")
#expected = "6:18 AM, Monday (20 days later)"