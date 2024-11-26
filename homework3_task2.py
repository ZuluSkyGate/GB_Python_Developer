# Задача 2. Поиск наибольшего числа в списке
# Напишите программу , которая принимает список чисел через строку и
# возвращает наибольшее число в этом списке.

numbers = [int(x) for x in input("Введите числа через пробел: ").split()]
max_number = numbers[0]

for num in numbers:
    if num > max_number:
        max_number = num
print(max_number)