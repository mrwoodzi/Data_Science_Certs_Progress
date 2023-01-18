hrs = input("Enter Hours:")
h = float(hrs)
rph = input("Enter Rate: ")
r = float(rph)

if h > 40 :
    reg = h * r
    otp = (h - 40) * (r * 0.5)
    actp = reg + otp
    
else:
	actp = h * r
print("Weekly Pay:", actp)