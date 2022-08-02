n= int(input("Enter a number: "))
def factorial(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else: 
        return n*factorial(n-1)
fact= factorial(n)
print("factorial of "+ str(n)+" " + "is:", fact)
