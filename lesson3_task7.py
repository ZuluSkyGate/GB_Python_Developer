# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.


# Решение 1

# text = input('Введите текст: ')
# result = {}
# for char in set(text):
#     result[char] = text.count(char)
#
# print(result)

# Решение 2 (без count)
#
# text = input('Введите текст: ')
# result = {}
# for char in text:
#     if char not in result:
#         result[char] = 1
#     else:
#         result[char] += 1
# print(result)

# Решение 3

text = input('Введите текст: ')
result2 = {}
for char in text:
    result2[char] = result2.get(char, 0) + 1
print(result2)