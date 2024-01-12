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

def print_report(path_to_file, num_words,chars_dict):
     print(f'''--- Begin report of {path_to_file} ---
          {num_words} words found in the document \n
{get_chars_report(chars_dict)}
          ''')