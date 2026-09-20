def count_words(text):
    words = text.split()
    return (len(words)) #counts how many words in the text

def character_count(text):
    character_counts = {}

    for character in text:
        character = character.lower() #turns every chracter into lowercase

        if character in character_counts:
            character_counts[character] += 1 #if the character is found in the dictionary increment it by 1
        else:
            character_counts[character] = 1 #if the character is not in the dictionary add it and = it to one count

    return character_counts


def sort_on(character_count: tuple[str, int]) -> int: #returns the count of each chracter 
    return character_count[1]


def chars_dict_to_sorted_list(character_counts: dict[str, int]) -> list[tuple[str, int]]: #turns dictionary into tuple
    characters = []

    for character in character_counts:
        count = character_counts[character]
        characters.append((character, count))

    return sorted(characters, reverse=True, key=sort_on) #sorts by frequency highest to lowest
