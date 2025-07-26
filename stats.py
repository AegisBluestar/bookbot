def get_num_words(book_text):
    book_word = book_text.split()
    return len(book_word)

def get_num_characters(book_text):
    
    num_characters_dict = {}
    book_text =  book_text.lower()
    list_characters = list(book_text)

    for character in list_characters:
        if character in num_characters_dict:
            num_characters_dict[character] += 1
        else:
            num_characters_dict[character] = 1

    return num_characters_dict

def sort_characters( num_characters_dict ):

    char_list = []
    for char, count in num_characters_dict.items():
        char_list.append( {"char": char, "num": count} )

    char_list.sort(reverse=True, key=sort_on)

    return char_list

def sort_on(items):
    return items["num"]