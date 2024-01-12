from helpers.book_helpers import *

def main():
    path_to_file = 'books/frankenstein.txt'
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_report(path_to_file, num_words, chars_dict)

main()