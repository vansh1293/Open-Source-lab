filename=input("Enter filename: ")
try:
    with open(filename, 'r') as file:
        lines = file.read()
        char_count = len(lines)
        print(f"Number of characters in '{filename}': {char_count}")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found!")
except Exception as e:
    print(f"Error: {e}")