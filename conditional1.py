time= int(input("Enter time"))
if(time>3 and time<12):
    print("Good Morning")
elif(time>=12 and time<16):
    print("Good Afternoon")
elif(time>=16 and time<20):
    print("Good Night")
else:
    print("Not Valid")