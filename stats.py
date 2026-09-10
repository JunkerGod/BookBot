def count_words(text):
    words = text.split()
    return (len(words))

def character_count(text):
    character_counts = {}

    for character in text:
        character = character.lower()

        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1

    return character_counts
    
