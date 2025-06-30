# Задание 1. Создайте массив размерностью 15. С помощью цикла for заполните массив
# случайными числами. Выведите элементы массива используя цикл foreach
import random
arr = [random.randint(1,100) for i in range(15)]
for i in arr:
    print(i)