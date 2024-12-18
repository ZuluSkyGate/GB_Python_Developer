# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно
from lesson1_task6 import BIG_LEAP_YEAR

BIN = 2
OCT = 8

num: int = int(input('Введите число: '))

for div in BIN, OCT:
    test_num: int = num
    res: str = ''
    while test_num:
        cur_num = test_num % div
        res = str(cur_num) + res
        test_num //= div
    print(f'для {div} {res = }')

