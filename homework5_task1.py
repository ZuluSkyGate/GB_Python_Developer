# Задание 1. Квадраты чисел
# Пользователь вводит число N. Напишите программу , которая генерирует
# последовательность из квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так
# далее). Реализацию напишите двумя способами: функция-генератор и
# генераторное выражение.

def generator_function(n: int):

    for number in range(1, n + 1):
        yield number ** 2

def main() -> None:

    n = int(input('Введите число N: '))

    print('Вывод квадратов. Функция-генератор')

    for square in generator_function(n):
        print(square, end=' ')
    print('\n')
    print('Вывод квадратов. Генераторное выражение')

    generator_expr = (i ** 2 for i in range(1, n + 1))

    for square in generator_expr:
        print(square, end=' ')
    print()
main()