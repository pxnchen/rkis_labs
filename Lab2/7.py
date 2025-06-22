# Задание 7. Напишите функцию для нахождения минимального элемента массива.
# Функция принимает целочисленный массив и возвращает число;
def min_element(arr):
    if not arr:
        return None
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val
arr = [2, 3, 1, 7, 5, 6]
empty_arr = []
print(min_element(arr))
print(min_element(empty_arr))