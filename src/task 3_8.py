# Задание 3_8
# Ввести число, проверить на то, что было введено именно число
# Возвести его в куб

num = (input('Введите число: '))
if num.isdigit():
    print('Отлично. Ниже приведено значение вашего числа в 3 степени:')
    print(int(num) ** 3)
else:
    print('Ошибка! Введено не число! Вы чё, цифры от букв отличить не можете?')