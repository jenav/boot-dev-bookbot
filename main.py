from stats import count_words


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


def main():
    book = "books/frankenstein.txt"
    print(f"--- Begin report of {book} ---")
    with open(book) as f:
        file_contents = f.read()
        wc = count_words(file_contents)
        print(f"{wc} words found in the document\n")
        chars_dict = count_characters(file_contents)
        sortd = sorted(chars_dict.items(), key=lambda x: x[1], reverse=True)
        for tuple in sortd:
            print(f"The '{tuple[0]}' character was found {tuple[1]} times")

        print("--- End report ---")


main()
