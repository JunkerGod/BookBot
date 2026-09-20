import sys

from stats import count_words, character_count, chars_dict_to_sorted_list

def get_book_text(path): #gets the book path and reads the contents
    with open(path) as f:
        return f.read()

def print_report(path, num_words, sorted_characters): #formats the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character, count in sorted_characters: #removes non-alphabetical characters
        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_ito_book>") #instructions on how to use the program
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words(text)
    character_counts = character_count(text)
    sorted_characters = chars_dict_to_sorted_list(character_counts)

    print_report(path, num_words, sorted_characters)

main()
