row = int(input("Enter no. of row:"))

for i in range(row+1):
    for j in range(i):
        print("*", end="")
    print(" ")