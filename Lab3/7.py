# Задание 7. Напишите функцию, которая принимает 1 число и определяет, расположены ли
# числа в нем по убыванию;
def descending_order(a):
    for i in range(len(str(a)) - 1):
        if str(a)[i] <= str(a)[i + 1]:
            return False
    return True
print(descending_order(67984))