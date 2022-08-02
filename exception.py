try:
    a= int(input("Enter First Number: "))
    b= int(input("Enter second Number: "))
    c= a/b
    print(c)
except Exception as e:
    print("Exception occured! please try with integer")
    print(e)

print("Thanks for using our software")