#с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено положительных
# и сколько отрицательных чисел.
a = 0
b = 0

while True:
    number = int(input())
    if number == 0:
        break
    if number > 0:
        a += 1
    elif number < 0:
        b += 1
print(a)
print(b)

