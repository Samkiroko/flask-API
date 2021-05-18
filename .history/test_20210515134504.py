list_of_words = [x.lower() for x in listofwords]

shortest_word_index = 0

# Find shortest word that exists in the list
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

print(longest_word)
