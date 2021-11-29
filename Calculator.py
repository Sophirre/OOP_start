from math import sin, cos, tan
import eel

eel.init("UI")


class Calculator:
    def __init__(self, mode):
        self.calc_mode = mode  # common, accounting, scientific

    @staticmethod
    def string_catcher(numbers: tuple) -> tuple:
        return tuple([num for num in numbers if isinstance(num, int) or isinstance(num, float)])

    @staticmethod
    def float_converter(*numbers):
        return tuple([num if isinstance(num, float) else float(num) for num in numbers])

    @staticmethod
    def int_converter(number: float):
        return int(number) if number % 1 == 0 else number

    def addition(self, numbers: tuple) -> float:
        numbers = self.string_catcher(numbers)
        result = numbers[0]
        for num in numbers[1:]:
            result = result + num
        return self.int_converter(result)

    def subtraction(self, numbers: tuple) -> float:
        numbers = self.string_catcher(numbers)
        result = numbers[0]
        for num in numbers[1:]:
            result = result - num
        return self.int_converter(result)

    def multiply(self, numbers: tuple) -> float:
        numbers = self.string_catcher(numbers)
        result = numbers[0]
        for num in numbers[1:]:
            result = result * num
        return self.int_converter(result)

    def division(self, numbers):
        result = numbers[0]
        for num in numbers[1:]:
            result = result / num
        return self.int_converter(result)

    @eel.expose
    def operation_chooser(self, operation, *numbers):
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
                raise e
        else:
            pass


class ScientificCalculator(Calculator):
    def operation_chooser(self, operation, *numbers):
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

    @classmethod
    def memory_get(cls):
        return cls.results

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
def show(v):
    return v


eel.start('index.html', size=(380, 600))
