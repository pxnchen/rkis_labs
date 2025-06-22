# Задание 10. Добавляйте новые элементы в список до тех пор,
# пока пользователь не отправит пустую строку.
# Выведите в консоль самый короткий и самый длинный элементы списка;
string = []
while True:
    input_ = input('add something: ')
    if input_ == '':
        break
    string.append(input_)
shortest = min(string, key=len)
print(shortest)
