n= int(input("Enter a number: "))
def natural(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else: 
        return n+natural(n-1)
nat= natural(n)
print("Sum of "+ str(n)+" "+"Natural Number" + "is:", nat)
