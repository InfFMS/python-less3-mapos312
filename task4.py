# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить сумму тех введённых чисел, которые делятся на 5.
a=0

while True:
    number = int(input())
    if number == 0:
            break
    if number % 5 == 0:
        a+=number
print (a)