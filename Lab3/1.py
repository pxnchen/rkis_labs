# Задание 1. Выведите на экран названия текущих дня недели и месяца, и свое имя. Каждое
# слово должно быть в отдельной строке;
from datetime import datetime
today = datetime.now()
name = 'Nikolay'
print("{}\n{}\n{}".format(today.strftime("%A"), today.strftime("%B"), name))