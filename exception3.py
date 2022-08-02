try:
    a= int(input("Enter First Number: "))
    c=1/a
    print(c)

except ValueError as e:
    print("Please Enter a valid number")
except ZeroDivisionError as e:
    print("Make sure you are not dividing by 0")
print("Thanks for using our software")