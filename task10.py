# с клавиатуры вводится число N, а затем – N натуральных чисел.
# Определить минимальное и максимальное среди простых чисел
# (которые делятся на сами не себя и на 1).
# Если таких чисел не было, вывести "нет".
def a(num): #ввел функцию которая будет проверять число на то простое оно или нет
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
N = int(input())
z = []
for _ in range(N):
    b = int(input())
    if a(b):
        z.append(b)
if z!=[]:
    min_z = min(z)
    max_z = max(z)
    print(f"Минимальное простое число: {min_z}")
    print(f"Максимальное простое число: {max_z}")
else:
    print("нет")





