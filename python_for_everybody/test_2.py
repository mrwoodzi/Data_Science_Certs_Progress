    #start_timeampm = start_part_day[-2:-1]
new_start = '2:59 '

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = new_start.rsplit(", ", 1)

# line 90 dlns_r = round(days_later_num, 2) #rounds the float from days_later_num
# line 97 new_time_day = round((int(hours_min)*.01)*24, 2)