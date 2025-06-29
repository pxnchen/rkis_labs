# Задание 8. Сгенерируйте массив(случайной длины, до 25-ти элементов) из чисел
# расположенных по убыванию, которые делятся на 3 без остатка
from random import randint
length = randint(1, 25)
arr = [i for i in range(length * 3, 0, -3)]
print(arr)
