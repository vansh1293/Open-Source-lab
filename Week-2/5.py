n = int(input("Enter a number: "))
num = []
for i in range(n):
    number = int(input(f"Enter number {i+1}: "))
    num.append(number)

count_dict = {}
for i in range(n):
    if num[i] in count_dict:
        count_dict[num[i]] += 1
    else:
        count_dict[num[i]] = 1
print("Duplicate numbers:")
duplicates_found = False
for number, count in count_dict.items():
    if count > 1:
        print(f"{number} appears {count} times")
        duplicates_found = True

if not duplicates_found:
    print("No duplicates found")