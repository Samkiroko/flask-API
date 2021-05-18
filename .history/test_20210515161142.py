
listofwords = ["7", "test", "tester", "Phenomenologically", "testertest",
               "testing", "TestingTester", "testingtester"]


list_of_words = [word.lower(), listofwords.remove(word.isdigit()) for word in listofwords]
print(list_of_words)

shortest_word_index = 0


for word in list_of_words:
    if len(word) < len(list_of_words[shortest_word_index]):
        shortest_word_index = list_of_words.index(word)


longword = list_of_words[shortest_word_index]
longword_list = []
longword_list.append(longword)

# Create a new list of all words containing the shortest word
for word in list_of_words:
    if len(longword) < len(word):
        checkword = ""
        for letter in word:
            checkword = checkword + letter
            if longword == checkword:
                longword_list.append(word)

# Finding the longest word in the new list
longest_word = ""
for lw in longword_list:
    if len(longest_word) < len(lw):
        longest_word = lw

if longest_word == longword:
    print("None")
else:
    print(listofwords[list_of_words.index(longest_word)])
