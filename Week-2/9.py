filename = input("Enter filename: ")
try:
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    print(f"Original file '{filename}':")
    print("".join(lines))
    print("File in reverse order:")
    for i in range(len(lines) - 1, -1, -1):
        print(lines[i], end="")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found!")
except Exception as e:
    print(f"Error: {e}")
