num = input("enter your number")
num= int(num)
total = 0

for i in range(0,num+1,1):    # here '0' for starting point and n+1 is higer limit and the last '1' is how many you want to increase.
    total = total + i

print(total)