def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    lower = text.lower()
    abc = {}
    for i in range(0, len(lower)):
        if not lower[i].isalpha():
            continue
        if lower[i] in abc:
            abc[lower[i]] += 1
        else:
            abc[lower[i]] = 1
    return abc
