def get_word_count(book_content):
    book_array = book_content.split()
    return len(book_array)

def get_character_count(book_content):
    char_dict = {}
    word_array = book_content.split()

    for word in word_array:
        for char in word:
            if char.lower() in char_dict:
                char_dict[char.lower()] += 1
            else:
                char_dict[char.lower()] = 1
    return char_dict

def sort_on(items):
    return items["count"]

def sort_dict(char_dict):
    char_list = []
    for key in char_dict:
        char_list.append({"char": key, "count": char_dict[key]})
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list

