from stats import get_num_words
from stats import get_num_characters
from stats import sort_characters
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text (book_filepath):
    
    with open(book_filepath) as f:
        file_content = f.read()
    return file_content

def stats_report(num_words, sorted_dict):
    
    print( "============ BOOKBOT ============" )
    print( "----------- Word Count ----------" )
    print( f"Found {num_words} total words" )
    print( "--------- Character Count -------" )
    for character in sorted_dict:
        if character["char"].isalpha():
            print ( character["char"]+": "+str(character["num"]) )
    




def main():
    
    book_text = get_book_text(sys.argv[1])
    num_words=get_num_words(book_text)
    num_characters_dict = get_num_characters(book_text)
    sorted_dict = sort_characters(num_characters_dict)
    
    #print ( f"{num_words} words found in the document" )
    #print ( num_characters_dict )

    stats_report(num_words, sorted_dict)
    

main()


