# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.


text = sorted(input('Enter a string: ').split())
# text.sort() Сохранять в переменную не надо

max_legth = 0
print(text)
for word in text:
    word_len = len(word)
    if max_legth < word_len:
        max_legth = word_len
for nn, word in enumerate(text, 1):
    print(f'{nn:>2}. {word:>{max_legth}}')