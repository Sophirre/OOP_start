class Calculator:
    def __init__(self, mode):
        calc_mode = mode  # common, accounting, scientific

    @staticmethod
    def addition(num1, num2):
        return num1 + num2

    @staticmethod
    def subtraction(num1, num2):
        return num1 - num2

    @staticmethod
    def multiply(num1, num2):
        return num1 * num2

    @staticmethod
    def division(num1, num2):
        return num1 / num2

    def operation_chooser(self, num1, num2, operation):
        if operation == '+':
            return Calculator.addition(num1, num2)
        elif operation == '-':
            return Calculator.subtraction(num1, num2)
        elif operation == '*':
            return Calculator.multiply(num1, num2)
        elif operation == '/':
            return Calculator.division(num1, num2)
        else:
            print("...")

calc1 = Calculator('common')
print(calc1.operation_chooser(20, 10, '+'))
print(calc1.operation_chooser(20, 10, '*'))
print(calc1.operation_chooser(20, 10, '-'))
print(calc1.operation_chooser(20, 10, '/'))
