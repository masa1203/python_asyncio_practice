words = ["Mon", "tue", "Web", "Thu", "fri", "sat", "sun"]


def change_words(words, func):
    for word in words:
        print(func(word))


def sample_func(word):
    return word.capitalize()


def sample_func2(word):
    return word.lower()


# sample_func = lambda word: word.capitalize()

# change_words(l, sample_func)

change_words(words, lambda word: word.capitalize())
change_words(words, lambda word: word.lower())
