nt_calc = 18085

if nt_calc >= 10080:
    days_later_num = (nt_calc/60)

dlns_r = round(days_later_num, 2)
print(dlns_r)
dlns_rs = str(dlns_r)
a, b = map(int,dlns_rs.split(".", 1))
a, b = [a],[b]
print(a, b)