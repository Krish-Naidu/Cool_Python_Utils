# Basic File Reader/Writer

def write_file(filename, text):
    file = open(filename, "w")
    file.write(text)
    file.close()
    print("File written!")

def read_file(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content

def append_file(filename, text):
    file = open(filename, "a")
    file.write(text)
    file.close()
    print("Content appended!")

# Call the functions
write_file("sample.txt", "Hello World!\nThis is a simple file.\n")

print("\nFile content:")
print(read_file("sample.txt"))

append_file("sample.txt", "This line was added!\n")

print("\nUpdated content:")
print(read_file("sample.txt"))
