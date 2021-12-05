from math import sin, cos, tan
import eel

eel.init("UI")


class Calculator:

    @staticmethod
    def string_catcher(numbers: tuple) -> tuple:
        return tuple([num if isinstance(num, int) or isinstance(num, float) else float(num) for num in numbers])

    @staticmethod
    def float_converter(*numbers):
        return tuple([num if isinstance(num, float) else float(num) for num in numbers])

    @staticmethod
    def int_converter(number: float):
        return int(number) if number % 1 == 0 else number

    @staticmethod
    @eel.expose
    def operation_checker(string: str) -> str:
        operator = None
        print(string)
        for el in string:
            if el == '/':
                operator = '/'
            elif el == '*':
                operator = '*'
            elif el == '+':
                operator = '+'
            elif el == '-':
                operator = '-'
            else: continue
        return operator

    @staticmethod
    @eel.expose
    def numbers_get(string):
        print(string)
        num_list = string.split(Calculator.operation_checker(string))
        num1 = num_list[0]
        num2 = num_list[1]
        print(tuple([num1, num2]))
        return tuple([num1, num2])

    def addition(self, numbers: tuple) -> float:
        numbers = self.string_catcher(numbers)
        print(f'string{numbers}')
        result = numbers[0]
        for num in numbers[1:]:
            result = result + num
        print(f'result: {result}')
        return result

    def subtraction(self, numbers: tuple) -> float:
        numbers = self.string_catcher(numbers)
        result = numbers[0]
        for num in numbers[1:]:
            result = result - num
        return result

    def multiply(self, numbers: tuple) -> float:
        numbers = self.string_catcher(numbers)
        result = numbers[0]
        for num in numbers[1:]:
            result = result * num
        return result

    def division(self, numbers):
        numbers = self.string_catcher(numbers)
        result = numbers[0]
        for num in numbers[1:]:
            result = result / num
        return round(result, 5)

    def operation_chooser(self, operation, numbers):
        if operation == '+':
            return self.addition(numbers)
        elif operation == '-':
            return self.subtraction(numbers)
        elif operation == '*':
            return self.multiply(numbers)
        elif operation == '/':
            try:
                return self.division(numbers)
            except ZeroDivisionError as e:
                return 'Error'
        else:
            pass

    @staticmethod
    @eel.expose
    def add_string(user_string, new):
        if user_string == "0":
            user_string = ''
        return user_string + new


class ScientificCalculator(Calculator):
    def operation_chooser(self, operation, numbers):
        super().operation_chooser(operation, numbers)
        if operation == 'sin':
            return sin(numbers[0])
        elif operation == 'cos':
            return cos(numbers[0])
        elif operation == 'tan' or operation == 'tg':
            return tan(numbers[0])


class AccountingCalculator(Calculator):
    results = []

    @classmethod
    def memory_add(cls, result):
        return cls.results.append(result)

    @property
    def memory_get(self):
        return self.results

    def addition(self, numbers):
        result = super().addition(numbers)
        AccountingCalculator.memory_add(result)
        return result

    def subtraction(self, numbers):
        result = super().subtraction(numbers)
        AccountingCalculator.memory_add(result)
        return result

    def division(self, numbers):
        result = super().division(numbers)
        AccountingCalculator.memory_add(result)
        return result

    def multiply(self, numbers):
        result = super().multiply(numbers)
        AccountingCalculator.memory_add(result)
        return result


@eel.expose
def object_init(calc_type, event, numbers):
    print(f'calc_type: {calc_type}')
    print(f'event: {event}')
    print(f'numbers: {numbers}')
    if calc_type == 'common':
        obj = Calculator()
    elif calc_type == 'sci':
        obj = ScientificCalculator()
    elif calc_type == 'accounting':
        obj = AccountingCalculator()
    else:
        obj = Calculator()
    try:
        return obj.operation_chooser(event, numbers)
    except AttributeError as e:
        return e


if __name__ == '__main__':
    eel.start('index.html', size=(380, 600))
    obj = AccountingCalculator()
    print('----CommonCalculator----\n')
    print(object_init('common', '+', 19.5, 180.5, '213', (2343, 23112)))
    print(object_init('common', '-', 19.5, 180.5, '213', (2343, 23112)))
    print(object_init('common', '*', 19.5, 180.5, '213', (2343, 23112)))
    print(object_init('common', '/', 20, 10, '213', (2343, 23112)))

    print('----ScientificCalculator----\n')
    print(f"Sin: {object_init('sci','sin', 360)}")
    print(f"Cos: {object_init('sci','cos', 520)}")
    print(f"Tan: {object_init('sci','tg', 60)}\n")
    print('----AccountingCalculator----\n')
    print(f'Addition: {object_init("accounting", "+", 100, 25.2, 25, 50)}')
    print(f'Subtraction: {object_init("accounting", "-", 100, 15, 25, 50)}')
    print(f'Multiply: {object_init("accounting", "*", 100, 25, 25, 50)}')
    print(f'Division: {object_init("accounting", "/", 100, 25, 25, 50)}')
    print(f'Memory: {obj.memory_get}\n')
    print('----------------------------')
