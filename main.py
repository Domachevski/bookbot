def main():
    # Выбор способа ввода текста
    print("Как вы хотите ввести текст?")
    print("1. Прочитать текст из файла.")
    print("2. Ввести текст вручную.")
    
    choice = input("Введите 1 или 2: ")

    if choice == "1":
        # Чтение текста из файла
        book_path = input("Введите путь к файлу: ")
        text = get_book_text(book_path)
    elif choice == "2":
        # Ввод текста вручную
        print("Введите текст:")
        text = input()
    else:
        print("Неверный выбор. Попробуйте снова.")
        return

    # Обработка текста
    word_count = words_counter(text)
    character_count = character_counter(text)
    char_list = chars_sorter(character_count)

    # Вывод отчёта
    print(f"<--- Begin report --->")
    print(f"Words in the text: {word_count}")
    print()
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("<--- End of report --->")

def get_book_text(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Файл по пути '{path}' не найден. Проверьте путь и повторите попытку.")
        return ""

def words_counter(text):
    words = text.split()
    word_count = len(words)
    return word_count

def character_counter(text):
    characters = {}
    low_string = text.lower()  # Преобразование текста в нижний регистр
    for char in low_string:
        if char.isalpha():  # Учитываем только буквы
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

def chars_sorter(characters):
    char_list = [{"char": char, "num": count} for char, count in characters.items()]
    char_list.sort(reverse=True, key=lambda x: x["num"])
    return char_list

# Запуск основной функции
if __name__ == '__main__':
    main()