import math


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

    @staticmethod
    def operation_chooser(operation, first_num, *numbers):
        if operation == '+':
            return Calculator.addition(first_num, numbers)
        elif operation == '-':
            return Calculator.subtraction(first_num, numbers)
        elif operation == '*':
            return Calculator.multiply(first_num, numbers)
        elif operation == '/':
            try:
                return Calculator.division(first_num, numbers)
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

'''
class AccountingCalculator(Calculator):
    results = []

    def addition(self, first_num, numbers):
        self.results = ['300']
        self.results.append(300)
        print(self.results)
    print(results) '''

if __name__ == '__main__':
    common = Calculator('common')
    science = ScientificCalculator('common')
    # accounting = AccountingCalculator('common')
    print('----CommonCalculator----')
    print(f"Multiply:  {common.operation_chooser('*', 20, 10)}")  # 200
    print(f"Subtraction: {common.operation_chooser('-', 340, 20, 40, 80)}")  # 200
    print(f"Addiction: {common.operation_chooser('+', 100, 25, 25, 50)}")  # 200
    print(f"Division: {common.operation_chooser('/', 400, 2)}")  # 200
    print('----ScientificCalculator----')
    print(f"Sin: {science.operation_chooser('sin', 360)}")
    print(f"Cos: {science.operation_chooser('cos', 520)}")
    print(f"Tan: {science.operation_chooser('tg', 60)}")
    # print('----AccountingCalculator----')
    # print(accounting.operation_chooser('+', 100, 25, 25, 50))
    # print(accounting.results)




