words = input("Text: ")
word_spacing = words.split( )
word_dictionary = {}

for word in word_spacing:
    if word in word_dictionary:
        word_dictionary[word] += 1
    else:
        word_dictionary[word] = 1
word_spacing = list(word_dictionary.keys())
word_spacing.sort()
max_length = max((len(word) for word in word_spacing))
for word in word_spacing:
    print("{:{}} : {}".format(word, max_length, word_dictionary[word]))
