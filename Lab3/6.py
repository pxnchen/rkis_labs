# Задание 6. Напишите функцию для нахождения произведения чисел, которые стоят на не
# четных местах
def multiplication(arr):
    k = 1
    for i in range(0, len(arr), 2):
        k *= arr[i]
    return k
print(multiplication([1, 2, 3, 4, 5]))