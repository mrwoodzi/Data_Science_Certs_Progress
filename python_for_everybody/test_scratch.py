 if days_later_num_unsplit > 2:
        for d in days_later_num_unsplit:
            days_later_list += 
        days_later, hours_min = map(int,dlns_rs.split(".", 1)) #splits float into days and percentage of a day
        #print(days_later, hours_min) # checking that I split the float
        days_later_str = str(days_later)
        #print(days_later_str)
        new_time_day = round((int(hours_min)*.01)*24, 2) # turning b back into decimal and figuring what time of the new day it is
        #print(new_time_day)
        new_time_day_str = str(new_time_day)
        hours, minutes_deci = map(int,new_time_day_str.split(".", 1))
        #print(hours, minutes_deci)
        #print(str(minutes_deci))
        minutes_int = round((minutes_deci * .01) * 60)
        new_minutes_day_str = str(minutes_int)
        new_minutes_day_str_len = len(new_minutes_day_str)
        if new_minutes_day_str_len == 1:
            new_minutes_day_str = '0' + new_minutes_day_str
        #print(new_minutes_day_str)
        while duration_time > 168: # this brings the orginal nt_calc down to a real number so we can figure out what day of the week it is
            #print(duration_time)
            duration_time = duration_time - 168
        next_day = (f' ({days_later_str} days later)')

print(x)

if day_of_week != True:
        nt_calc = ampm_minutes_old + duration_time
        if nt_calc < 1439:
            if nt_calc <= 719: #deals with time adding but not going to next day
                new_ampm = ' AM'
                next_day = ''
            elif nt_calc >= 720:
                new_ampm = ' PM'
                next_day = ''
        elif nt_calc >= 1440 <= 2879:
            next_day = ' (next day)'
            if nt_calc <= 2159: #deals with time adding but not going to next day
                new_ampm = ' AM'
            elif nt_calc >= 2160:
                new_ampm = ' PM'
        elif nt_calc >= 2880 <= 4319:

            if nt_calc <= 3599: #deals with time adding but not going to next day
                new_ampm = ' AM'
            elif nt_calc >= 3600:
                new_ampm = ' PM'
        elif nt_caltc >= 4320:
            next_day = (f' {days_later_str} days later')

 + old_start_time_day) / 24