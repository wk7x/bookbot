filepath = "books/frankenstein.txt"
def word_counter(words):
    return len(words.split())

def char_counter(words):
    char_dict = {}
    for char in words:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1
    return char_dict

def sorted_char_counter_list(char_counts):
    sorted_list = []
    for key in char_counts.keys():
        if key.isalpha():
            sorted_list.append((key, char_counts[key]))
    sorted_list.sort(key=lambda x: x[1], reverse=True)
    return sorted_list

with open(filepath) as f:
    contents = f.read()
    word_count = word_counter(contents)
    char_counts = char_counter(contents) 
    sorted_char_counts = sorted_char_counter_list(char_counts)

    print(f"--- Begin report of {filepath} ---")
    print(f"{word_count} words found in the document\n")
    for char_count in sorted_char_counts:
        print(f"The '{char_count[0]}' character was found {char_count[1]} times")
    print("--- End report ---")