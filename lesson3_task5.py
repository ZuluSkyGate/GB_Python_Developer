# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

# 1

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

unique_list = []

for n, item in enumerate(data, 1):
    if item % 2:
        unique_list.append(n)
print(unique_list)

# 2

# data1 = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42]
#
# new_list = []
# length = len(data1)
# new_list = [i + 1 for i in range(length) if data1[i] % 2]
# print(new_list)

# 3

# data1 = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42]

# new_list = [n for n, el in enumerate(data1, 1) if el % 2]