

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
            next_day = ' (2 days later)'
            if nt_calc <= 3599: #deals with time adding but not going to next day
                new_ampm = ' AM'
            elif nt_calc >= 3600:
                new_ampm = ' PM'
        elif nt_caltc >= 4320:
            next_day = (f' {days_later_str} days later')

    if day_of_week == True:
        if day_of_week_str_lower <= 1439:
            new_day_week = 'Sunday'
            minutes_in_week = ampm_minutes_old 
        elif day_of_week_str_lowe >= 1440 <= 2879:
            new_day_week = 'Monday'
            minutes_in_week = 1440 + ampm_minutes_old 
        elif day_of_week_str_lowe >= 2880 <= 4319:
            new_day_week = 'Tuesday'
            minutes_in_week = 2880 + ampm_minutes_old 
        elif day_of_week_str_lowe >= 4320<= 5759:
            new_day_week = 'Wednesday'
            minutes_in_week = 4320 + ampm_minutes_old 
        elif day_of_week_str_lowe >= 5760 <= 7199:
            new_day_week = 'Thursday'
            minutes_in_week = 5760 + ampm_minutes_old
        elif day_of_week_str_lowe >= 7200<= 8639:
            new_day_week = 'Friday'
            minutes_in_week = 7200 + ampm_minutes_old
        elif day_of_week_str_lowe >= 8640 <= 10079:
            new_day_week = 'Saturday'
            minutes_in_week = 8640 + ampm_minutes_old