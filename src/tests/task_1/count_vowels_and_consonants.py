def is_russian_word(word):
    """Проверяет, что слово состоит только из русских букв"""
    return all('а' <= letter <= 'я' for letter in word.lower())


def count_vowels(word):
    vowels = 'аоиеёэыуюя'
    exceptions = 'ъь'
    result_vowel = 0
    result_exceptions = 0
    for letter in word.lower():
        if letter in vowels:
            result_vowel += 1
        elif letter in exceptions:
            result_exceptions += 1

    return (result_vowel, result_exceptions)


def count_vowels_and_consonants(word):
    vowels_and_exceptions_count = count_vowels(word)

    return [vowels_and_exceptions_count[0], len(word) - vowels_and_exceptions_count[0] - vowels_and_exceptions_count[1]]


def main():
    while True:
        word = input('Введите слово: ').lower()
        if not is_russian_word(word):
            print('Ошибка, введите слово на кириллице')
            continue
        result = count_vowels_and_consonants(word)
        print(f'Гласных: {result[0]}\nСогласных: {result[1]}')


if __name__ == '__main__':
    main()
