import math
import eel

eel.init("UI")



class Calculator:
    def __init__(self, mode):
        self.calc_mode = mode  # common, accounting, scientific

    @staticmethod
    def addition(first_num, numbers):
        if isinstance(first_num, int):
            result = first_num
            for num in numbers:
                if isinstance(num, int):
                    result = result + num
                else:
                    raise Exception('The argument must be an integer')
        else:
            raise Exception('The argument must be an integer')
        return result

    @staticmethod
    def subtraction(first_num, numbers):
        if isinstance(first_num, int):
            result = first_num
            for num in numbers:
                if isinstance(num, int):
                    result = result - num
                else:
                    raise Exception('The argument must be an integer')
        else:
            raise Exception('The argument must be an integer')
        return result

    @staticmethod
    def multiply(first_num, numbers):
        if isinstance(first_num, int):
            result = first_num
            for num in numbers:
                if isinstance(num, int):
                    result = result * num
                else:
                    raise Exception('The argument must be an integer')
            return result
        else:
            raise Exception('The argument must be an integer')

    @staticmethod
    def division(first_num, numbers):
        if isinstance(first_num, int):
            result = first_num
            for num in numbers:
                result = result / num
                if result % num == 0:  # Когда деление с остатком в консоль выводиться число с плавоющей точкой
                    result = int(result)
        else:
            raise Exception('The argument must be a integer')
        return result

    @eel.expose
    def operation_chooser(self, operation, first_num, *numbers):
        if operation == '+':
            return self.addition(first_num, numbers)
        elif operation == '-':
            return self.subtraction(first_num, numbers)
        elif operation == '*':
            return self.multiply(first_num, numbers)
        elif operation == '/':
            try:
                return self.division(first_num, numbers)
            except ZeroDivisionError as e:
                raise e
        else:
            pass


class ScientificCalculator(Calculator):
    def operation_chooser(self, operation, first_num):
        super().operation_chooser(operation, first_num)
        if operation == 'sin':
            return math.sin(first_num)
        elif operation == 'cos':
            return math.cos(first_num)
        elif operation == 'tan' or operation == 'tg':
            return math.tan(first_num)


class AccountingCalculator(Calculator):
    results = []

    @classmethod
    def memory_add(cls, result):
        return cls.results.append(result)

    @classmethod
    def memory_get(cls):
        return cls.results

    def addition(self, first_num, numbers):
        result = super().addition(first_num, numbers)
        AccountingCalculator.memory_add(result)
        return result

    def subtraction(self, first_num, numbers):
        result = super().subtraction(first_num, numbers)
        AccountingCalculator.memory_add(result)
        return result

    def division(self, first_num, numbers):
        result = super().division(first_num, numbers)
        AccountingCalculator.memory_add(result)
        return result

    def multiply(self, first_num, numbers):
        result = super().multiply(first_num, numbers)
        AccountingCalculator.memory_add(result)
        return result


@eel.expose
def show(v):
    return v

eel.start('index.html', size=(380, 600))