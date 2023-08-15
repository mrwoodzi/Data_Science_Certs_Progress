hrs = input("Enter Hours: ")
rph = input("Enter Rate: ")

try:   
    h = float(hrs)
    r = float(rph)
except:
    print("Error, please enter a numeric input!")
    quit()

if h > 40 :
    reg = h * r
    otp = (h - 40) * (r * 0.5)
    actp = reg + otp
    
else:
	actp = h * r
print("Weekly Pay:", actp)