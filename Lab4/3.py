# Задание 3. Напишите enum для математических операций (+, -, *, /). Создайте функцию,
# которая будет принимать 2 числа и операцию. Внутри функции создайте switch, который
# будет содержать case для каждой операции. Функция должна возвращать 4 значения
# (firstNumber, secondNumber, operation, result)
import enum

class MathOperation(enum.Enum):
    ADD = '+'
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
def calculation(firstNumber: int, secondNumber: int, operation: MathOperation):
    result = None
    match operation:
        case MathOperation.ADD:
            result = firstNumber + secondNumber
        case MathOperation.SUBTRACT:
            result = firstNumber - secondNumber
        case MathOperation.MULTIPLY:
            result = firstNumber * secondNumber
        case MathOperation.DIVIDE:
            if secondNumber == 0:
                raise ValueError('Деление на ноль невозможно!')
            result = firstNumber / secondNumber
    return (firstNumber, secondNumber, operation.value, result)
a = 10
b = 5
operation = MathOperation.ADD

firstNum, secondNum, op, res = calculation(a,b,operation)
print(f'{firstNum} {op} {secondNum} = {res}')