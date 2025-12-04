num= None
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
num = int(input("Enter a number to compute its factorial: "))
print(fact(num))  # Output: 24