# Задание 3. Напишите функцию, для нахождения количества квадратов, которые можно
# вырезать из прямоугольника определенного размера. Например, функция принимает
# размеры прямоугольника(два числа) и размер стороны квадрата(одно число), а
# возвращает число квадратов, которые можно вырезать из прямоугольника
def count_square(a,b,c):
    if a < c or b < c:
        return 0
    elif a // c > 1 and b // c > 1:
        return b // c * a // c
    elif a // c == 1:
        return b // c
    elif b // c == 1:
        return a // c
print(count_square(3,4,3))