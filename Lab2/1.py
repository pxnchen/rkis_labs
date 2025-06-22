# Задание 1. Создайте целочисленную коллекцию.
# Добавьте в нее 10 случайных чисел.
# Выведите в консоль минимальный элемент коллекции;

from random import randint
collection = []
for i in range(0, 10):
    collection.append(randint(1, 100))
print(collection)
print(min(collection))