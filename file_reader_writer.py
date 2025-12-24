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

write_file("sample.txt", "Hello World!\nThis is a simple file.")

print("File content:")
print(read_file("sample.txt"))
