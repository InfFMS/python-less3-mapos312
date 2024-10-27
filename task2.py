# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено двузначных натуральных чисел,
# и сколько других.
a=0
b=0
while True:
    number = int(input())
    if number == 0:
        break
    if number >= 10 and number <= 99:
        a+=1
    else: b+=1
print(a)
print(b)
