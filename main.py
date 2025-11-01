from stats import get_num_words, get_num_chars, get_sorted_dictionary_list
import sys


def get_book_text(filepath: str):
    with open(filepath) as f:
        return f.read()


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    relpath = sys.argv[1]
    num_chars = get_num_chars(get_book_text(relpath))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {relpath}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(relpath)} total words")
    print("--------- Character Count -------")
    for d in get_sorted_dictionary_list(num_chars):
        if d["char"].isalpha():
            print(f"{d['char']}: {d['num']}")


main()
