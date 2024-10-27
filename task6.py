# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить минимальное и максимальное из введённых чисел.
def maxi(mas):
    maximum=mas[0]
    for i in range(1,len(mas)):
        if mas[i]>maximum:
            maximum=mas[i]
    return maximum
def mini(mas):
    minimum=mas[0]
    for i in range(1,len(mas)):
        if mas[i]<minimum:
            minimum=mas[i]
    return minimum
a = []
while True:
    b = int(input())
    if b == 0:
        break
    a.append(b) # добавляю числа b в список a
if a:
    print(f"Минимальное число: {mini(a)}")
    print(f"Максимальное число: {maxi(a)}")
