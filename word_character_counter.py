text = input("Enter your text: ")

char_count = 0
for char in text:
    char_count += 1

word_count = 0
words = text.split(" ")
for word in words:
    word_count += 1

print(word_count)
print(char_count)
