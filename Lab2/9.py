# Задание 9. Напишите функция, которая определяет наибольшее из двух чисел;
def largest_num(a, b):
    if a>b:
        return a
    elif a<b:
        return b
    else:
        return None