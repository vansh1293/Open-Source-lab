def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
n = int(input("Enter a number: "))
if n < 0:
    print("Fibonacci sequence is not defined for negative numbers.")
else:
    print("Fibonacci sequence up to", n, "is:")
    for i in range(n+1):
        print(fib(i), end=" ")