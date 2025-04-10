import sys
from stats import count_words, get_count_of_chars, sort_dictionary

def main():
    text = get_book_text(sys.argv[1])
    count_of_words = count_words(text)
    chars_dict = get_count_of_chars(text)
    tuple_dict_list = list(chars_dict.items())
    sorted_dict = sort_dictionary(tuple_dict_list)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_of_words} total words")
    print("--------- Character Count -------")

    for char in sorted_dict:
        if char["char"].isalpha():
            print(f'{char["char"]}: {char["count"]}')
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    raise sys.exit(1)

main()
