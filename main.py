def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    word_count = words_counter(text)
    character_count = character_counter(text)
    char_list = chars_sorter(character_count)
    print( f"<--- Begin report of {book_path} --->")
    print(f"Words in a book:{word_count}")
    print()
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def words_counter(text):
    words = text.split()
    word_count = len(words)
    return word_count

def character_counter(text):
    characters = {}
    my_string = text
    low_string = my_string.lower()
    for i in low_string:
        if i in characters:
            characters[i] += 1
        else:
            characters[i] = 1
    return characters

def chars_sorter(characters):
    char_list = []
    for char, count in characters.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=lambda x: x["num"])  
    return char_list
main()