# Даны действительные числа x и y. Получить |x| − |y| / 1+ |xy|
# Задание 2
x = 6
y = -8
result = (abs(x) - abs(y)) / (1 - abs(x * y))
print("Result is: ", result)