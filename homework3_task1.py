# Задание 1. Удаление дубликатов из списка
# Дан список повторяющихся элементов. Вернуть список с дублирующимися
# элементами. В результирующем списке не должно быть дубликатов.

elements = [1, 2, 2, 3, 4, 4, 4, 5, 5]
duplicates = []

for x in elements:
    if elements.count(x) > 1 and x not in duplicates:
        duplicates.append(x)
print(duplicates)