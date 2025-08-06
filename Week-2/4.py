n = int(input("Enter a number: "))
num = [] 
for i in range(n):
    number = int(input(f"Enter number {i+1}: "))
    num.append(number)  
for i in range(n):
    if num[i] % 2 == 0:
        print(f"{num[i]} is even")

