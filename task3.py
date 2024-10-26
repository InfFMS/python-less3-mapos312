# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено простых натуральных чисел
# (которые делятся только сами на себя и на 1), и сколько составных.
a=0
b=0
while True:
    number = int(input())
    if number == 0:
        break
    elif number == 2:
        a+=1
    elif number == 1:
        continue
    else:
        x=True   # x-предположение, что число простое, если это не так, мы выходим из цикла
        for i in range(2, (int (number ** 0.5) +1)):
            if number % i == 0:
                b+=1
                x = False
                break
        if x:
            a+=1


print(a)
print(b)
