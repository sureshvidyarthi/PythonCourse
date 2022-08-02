n= int(input("Enter a number: "))
def square(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else: 
        return n*n+square(n-1)
nat= square(n)
print("Sum of square of "+ str(n)+" "+"Natural Number" + "is:", nat)
