# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

REFORM = 1582
BIG_LEAP_YEAR = 400
SMALL_LEAP_YEAR = 4
LARGE_NOT_LEAP_YEAR = 100
ZERO = 0

year = int(input('Введите год: '))

if REFORM > year:
    result = 'Григорианский календарь ещё не введён'
elif year % BIG_LEAP_YEAR == ZERO:
    result = f'{year} - Високосный год'
elif year % LARGE_NOT_LEAP_YEAR == ZERO:
    result = f'{year} - Не високосный год'
elif year % SMALL_LEAP_YEAR == ZERO:
    result = f'{year} - Високосный год'
else:
    result = f'{year} - Не високосный год'
print(result)