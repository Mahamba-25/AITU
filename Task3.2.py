words = []

while True:
    word = input("Enter a word (press Enter to finish): ")

    if not word:
        break

    words.append(word)

sorted_words = sorted(set(words))

for word in words:
    print(word)
