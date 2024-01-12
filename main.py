def main():
    path_to_file = 'books/frankenstein.txt'
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f'''--- Begin report of {path_to_file} ---
          {num_words} words found in the document 
{get_chars_report(chars_dict)}
          ''')


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_chars_dict(text):
    chars = {}

    for characters in text:
        lowered = characters.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_chars_report(dict):
    char_list = []
    for char in dict:
        if char.isalpha():
            char_list.append(f"The '{char}' was found {dict[char]} times ")
    return "\n".join(sorted(char_list))


main()