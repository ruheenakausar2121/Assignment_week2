text = input("Enter a text: ")
words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Word Frequencies:")
for word, count in freq.items():
    print(word, ":", count)
