number = int(input("Enter a number: "))
for x in range(1,11):
    table = number*x
    print(table)
    with open("file.txt","a") as f:
        f.write(str(table))