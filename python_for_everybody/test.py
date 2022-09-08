nt_calc = 18085

if nt_calc >= 10080:
    days_later_num = ((nt_calc/60)/24) #gives me number of days later
    print(str(days_later_num))
    dlns_r = round(days_later_num, 2) #rounds the float from days_later_num
    print(dlns_r)
    dlns_rs = str(dlns_r)
    a, b = map(int,dlns_rs.split(".", 1)) #splits float into days and percentage of a day
    print(a, b) # checking that I split the float
    days_later = str(a)
    new_time_day = round((int(b)*.01)*24, 2) # turning b back into decimal and figuring what time of the new day it is
    print(new_time_day)
    print(f'({days_later} days later)')
    while nt_calc > 10080:
        nt_calc = nt_calc - 10080
    print(str(nt_calc))

