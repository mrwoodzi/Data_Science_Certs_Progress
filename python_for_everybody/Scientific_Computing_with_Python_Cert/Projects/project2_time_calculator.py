def add_time(start, duration, day_of_week=None):
    start_s = ""
    duration_d = ""
    old_start_time_day = None
    new_day_week = ""
    new_ampm = ""
    next_day = ""
    new_time = ""
    new_hour_day_str = ""
    new_minutes_day_str = ""
    new_day_week = ""
    dots = ":"
    comma = ""
    for a in start:
        start_s += a
    ampm = start_s[-2] + start_s[-1]  # We extract if it's am or pm
    for b in duration:
        duration_d += b
    fds = str(
        list(pos for pos, char in enumerate(start_s) if char == dots)
    )  # finds : in start
    fdd = str(
        list(pos for pos, char in enumerate(duration_d) if char == dots)
    )  # finds : in duration
    fds_int = int(fds[1])
    fdd_int = int(fdd[1])
    nss_h_int = int(start_s[0:(fds_int)])  # starting hour 3
    nss_m_int = int(start_s[fds_int + 1 : fds_int + 3])  # starting min 30
    nds_h_int = int(duration_d[0:(fdd_int)])  # duration hour 2
    nds_m_int = int(duration_d[fdd_int + 1 : fdd_int + 3])  # duration min 12

    if ampm == "AM":
        old_start_time_day = nss_h_int + float(
            nss_m_int / 60
        )  # puts start time hours into minutes
    elif ampm == "PM":
        old_start_time_day = (
            12 + nss_h_int + float(nss_m_int / 60)
        )  # puts start time hours into minutes
    duration_time_hours = nds_h_int + (nds_m_int / 60)

    # this gives me the total number of days later and gives me the hours of the next day in decimal form
    days_later_num_unsplit = duration_time_hours / 24
    days_later_int_deci_str = str((duration_time_hours + old_start_time_day) / 24)
    days_later_str, nope = map(int, days_later_int_deci_str.split(".", 1))
    days_later_int = int(days_later_str)
    days_later_num_unsplit_str = str(days_later_num_unsplit)
    old_days_later_str, hours_in_day_deci_int = map(
        int, days_later_num_unsplit_str.split(".", 1)
    )
    hours_in_day_deci_int_float = days_later_num_unsplit % 1
    hours_in_day_deci_str = str(hours_in_day_deci_int_float)
    hours_in_day_deci_str = hours_in_day_deci_str[0:6]
    new_minutes_day_int = hours_in_day_deci_int_float * 24

    # this gives me my minutes and starts the hour process
    hours_later_military_deci = old_start_time_day + new_minutes_day_int
    new_minutes_day_military_deci = hours_later_military_deci % 1  # minutes in decimal
    new_minutes_day_military = round(new_minutes_day_military_deci * 60)
    new_minutes_day_str = str(new_minutes_day_military)

    # gives me the new hour time
    hours_later_military_deci_str = str(hours_later_military_deci)
    hours_later_military, nothing = map(
        int, hours_later_military_deci_str.split(".", 1)
    )

    len_minutes = len(new_minutes_day_str)  # gives me len of minutes
    if len_minutes == 1:
        new_minutes_day_str = "0" + new_minutes_day_str
    elif len_minutes == 0:
        new_minutes_day_str = "00"
    hours_later_military_new_day = hours_later_military

    if days_later_int > 2:
        next_day = f" ({days_later_str} days later)"
        if hours_later_military_new_day > 25:
            hours_later_military_new_day = hours_later_military_new_day - 24
        if hours_later_military_new_day == 24:
            new_ampm = " AM"
        if hours_later_military_new_day == 0:
            hours_later_military_new_day = 12
        if hours_later_military_new_day <= 11:
            if hours_later_military_new_day <= 11:
                new_hour_day = hours_later_military_new_day
                new_hour_day_str = str(new_hour_day)
                new_ampm = " AM"
            elif hours_later_military_new_day >= 12 <= 23:
                new_hour_day = hours_later_military_new_day - 12
                new_hour_day_str = str(new_hour_day)
                new_ampm = " PM"
    elif days_later_int == 2:
        next_day = " (2 days later)"
        if hours_later_military_new_day > 25:
            hours_later_military_new_day = hours_later_military_new_day - 24
        # print(str(hours_later_military_new_day))
        if hours_later_military_new_day == 24:
            new_hour_day_str = "12"
            new_ampm = " AM"
        elif hours_later_military_new_day <= 11:
            if hours_later_military_new_day <= 11:
                new_hour_day = hours_later_military_new_day
                # print(str(new_hour_day))
                new_hour_day_str = str(new_hour_day)
                new_ampm = " AM"
            elif hours_later_military_new_day >= 12 <= 23:
                # print(hours_later_military)
                new_hour_day = hours_later_military_new_day - 12
                # print(new_hour_day)
                new_hour_day_str = str(new_hour_day)
                new_ampm = " PM"
    elif days_later_int == 1:
        next_day = " (next day)"
        if hours_later_military_new_day > 25:
            hours_later_military_new_day = hours_later_military_new_day - 24
        if hours_later_military_new_day > 24:
            hours_later_military_new_day = hours_later_military_new_day - 24
        if hours_later_military_new_day == 24:
            new_hour_day_str = "12"
            new_ampm = " AM"
        elif hours_later_military_new_day <= 11:
            if hours_later_military_new_day <= 11:
                new_hour_day = hours_later_military_new_day
                # print(str(new_hour_day))
                new_hour_day_str = str(new_hour_day)
                new_ampm = " AM"
            elif hours_later_military_new_day >= 12 <= 23:
                # print(hours_later_military)
                new_hour_day = hours_later_military_new_day - 12
                # print(new_hour_day)
                new_hour_day_str = str(new_hour_day)
                new_ampm = " PM"
    elif days_later_int == 0:
        next_day = ""
        if hours_later_military_new_day <= 11:
            new_hour_day = hours_later_military
            # print(str(new_hour_day))
            new_hour_day_str = str(new_hour_day)
            new_ampm = " AM"
        elif hours_later_military_new_day >= 12 <= 23:
            new_ampm = " PM"
            if hours_later_military_new_day == 12:
                new_hour_day_str = hours_later_military_new_day
            else:
                # print(hours_later_military)
                new_hour_day = hours_later_military_new_day - 12
                # print(new_hour_day)
                new_hour_day_str = str(new_hour_day)

    if day_of_week:
        comma = ","
        day_of_week_str_lower = str.lower(day_of_week)
        if day_of_week_str_lower == "sunday":
            day_of_week_int_hrs = 0
        elif day_of_week_str_lower == "monday":
            day_of_week_int_hrs = 24
        elif day_of_week_str_lower == "tuesday":
            day_of_week_int_hrs = 48
        elif day_of_week_str_lower == "wednesday":
            day_of_week_int_hrs = 72
        elif day_of_week_str_lower == "thursday":
            day_of_week_int_hrs = 96
        elif day_of_week_str_lower == "friday":
            day_of_week_int_hrs = 120
        elif day_of_week_str_lower == "saturday":
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
            new_day_week = " Sunday"
        elif old_start_time_day_week >= 24 and old_start_time_day_week < 48:
            new_day_week = " Monday"
        elif old_start_time_day_week >= 48 and old_start_time_day_week < 72:
            new_day_week = " Tuesday"
        elif old_start_time_day_week >= 72 and old_start_time_day_week < 96:
            new_day_week = " Wednesday"
        elif old_start_time_day_week >= 96 and old_start_time_day_week < 120:
            new_day_week = " Thursday"
        elif old_start_time_day_week >= 120 and old_start_time_day_week < 144:
            new_day_week = " Friday"
        elif old_start_time_day_week >= 144 and old_start_time_day_week < 168:
            new_day_week = " Saturday"

    new_time = f"{new_hour_day_str}{dots}{new_minutes_day_str}{new_ampm}{comma}{new_day_week}{next_day}"

    return new_time


# Testing if it works correctly
print(add_time("8:16 PM", "466:02", "tuesday"))
# actual = add_time("8:16 PM", "466:02", "tuesday")
# expected = "6:18 AM, Monday (20 days later)"
