word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

sorted_word1 = sorted(word1.lower())
sorted_word2 = sorted(word2.lower())

if sorted_word1 == sorted_word2:
    print("Anagrams!")
else:
    print("Not anagrams.")
