# 1. check the frequency of words appear in the paragraph using dictionary


from collections import Counter


def word_frequency(paragraph):
    words = paragraph.split()
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies


paragraph = "welcome to the world of high level programming language Python.Python is the simple,easy to unserstand language.Python is Dyanamic language"
frequencies = word_frequency(paragraph)
print(f"Word frequencies: {frequencies}")

# 1. check the frequency of words appear in the paragraph using Counter


def word_frequencies(paragraph):
    words = paragraph.split()
    return Counter(words)


paragraph = "welcome to the world of high level programming language Python.Python is the simple,easy to unserstand language.Python is Dyanamic language"
frequencies = word_frequencies(paragraph)
print(f"Word frequencies: {frequencies}")


# 2. Search the word from the paragraph


def words_starting_with(paragraph, letter):
    words = paragraph.split()
    return [word for word in words if word.startswith(letter)]


paragraph = "welcome to the world of high level programming language Python . Python is the simple,easy to unserstand language. Python is Dyanamic language"
letter = "Python"
starting_with_letter = words_starting_with(paragraph, letter)
print(f"Words starting with '{letter}': {starting_with_letter}")
