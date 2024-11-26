# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.
from enum import unique

data = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42]

unique_list = [item for item in data if data.count(item) != 2]
print(unique_list)

# 2
# data1 = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42]

# for item in data1:
#     if data.count(item) != 2:
#         unique_list.append(item)
# print(unique_list)

# 3
# data2 = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42]

# COUNT = 2
#
# for item in set(data2):
#     if data.count(item) == COUNT:
#         for _ in range(COUNT):
#             data2.remove(item)
# print(f'{data2 = }')
