filename = input("Enter filename: ")
new_text = "Hi, I am currently pursuing my BTech from Jaypee."
try:
    file = open(filename, 'r')
    original_content = file.read()
    file.close()
    print("Original content:")
    print(original_content)
except:
    print("File doesn't exist. Creating new file.")
file = open(filename, 'w')
file.write(new_text)
file.close()
print("File updated successfully!")
file = open(filename, 'r')
updated_content = file.read()
file.close()
print("New content:")
print(updated_content)
