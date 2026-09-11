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


def sort_on(character_count: tuple[str, int]) -> int:
    return character_count[1]


def chars_dict_to_sorted_list(character_counts: dict[str, int]) -> list[tuple[str, int]]:
    characters = []

    for character in character_counts:
        count = character_counts[character]
        characters.append((character, count))

    return sorted(characters, reverse=True, key=sort_on)
