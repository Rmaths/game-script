def count_words(words):
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    return word_counts


words = input("Enter list of words: ")
words = words.split()
word_countss = count_words(words)
print(word_countss)