# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в верхнем регистре в остальных случаях.
# 3.15, -4.56, .78, 143.

data = input(f'Введите данные: ')

if data.isdigit():
    result = int(data)
elif data.replace(".", "").replace("-", "").isdigit() \
    and data.count(".") < 2 and "-" not in data[1:]:
    result = float(data)
elif not data.islower():
    result = data.lower()
else:
    result = data.upper()
print(f"{result = }")