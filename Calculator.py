class Calculator:
    def __init__(self, mode):
        self.calc_mode = mode  # common, accounting, scientific

    @staticmethod
    def addition(num1, num2):
        if isinstance(num1, int) and isinstance(num2, int):
            return num1 + num2
        else: 
            raise Exception('The argument must be an integer')

    @staticmethod
    def subtraction(num1, num2):
        if isinstance(num1, int) and isinstance(num2, int):
            return num1 - num2
        else: 
            raise Exception('The argument must be an integer')

    @staticmethod
    def multiply(num1, num2):
        if isinstance(num1, int) and isinstance(num2, int):
            return num1 * num2  
        else: 
            raise Exception('The argument must be an integer')
    
    @staticmethod
    def division(num1, num2):
        if isinstance(num1, int) and isinstance(num2, int):
            result = num1 / num2
            if num1 % num2 != 0:
                return result
            else:
                return int(result)
        else:
            raise Exception('The argument must be a integer')
    
    def operation_chooser(self, num1, num2, operation):
        if operation == '+':
            return Calculator.addition(num1, num2)
        elif operation == '-':
            return Calculator.subtraction(num1, num2)
        elif operation == '*':
            return Calculator.multiply(num1, num2)
        elif operation == '/':
            try:
                return Calculator.division(num1, num2)
            except ZeroDivisionError as e:
                print(e)
        else:
            print("...")

calc1 = Calculator('common')
print(calc1.operation_chooser(9, 3, '+'))
print(calc1.operation_chooser(9, 3, '-'))
print(calc1.operation_chooser(9, 3, '*'))
print(calc1.operation_chooser(9, 3, '/'))
