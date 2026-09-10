from stats import count_words, character_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    character_counts = character_count(text)

    print(f"Found {num_words} total words")
    print(character_counts)

main()
