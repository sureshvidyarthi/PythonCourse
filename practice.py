while(True):
    print("Press q to quit")
    number = int(input("Enter a number: "))
    if number=='q':
        break
    try:
        number=int(number)
        if number>10:
            print("You entered a number greater than 10")
        else:
            print("You entered a number less than 10")
    except Exception as e:
        print(f"Your input resulted is an error {e}")
print("Thanks for entering a number")