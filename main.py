import sys
from stats import count_words, count_characters


def usage():
    print("Usage: python3 main.py <path_to_book>")


def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")

    with open(sys.argv[1]) as f:
        file_contents = f.read()

        wc = count_words(file_contents)
        print("----------- Word Count ----------")
        print(f"Found {wc} total words")

        chars_dict = count_characters(file_contents)
        sortd = sorted(chars_dict.items(), key=lambda x: x[1], reverse=True)

        print("--------- Character Count -------")
        for tuple in sortd:
            print(f"{tuple[0]}: {tuple[1]}")

        print("============= END ===============")


main()
