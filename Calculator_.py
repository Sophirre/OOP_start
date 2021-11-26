from math import sin, cos, tan, sqrt
from abc import ABC, abstractmethod
import types

import eel


class Calculator(ABC):
    @staticmethod
    def string_catcher(*numbers) -> list:
        return [num for num in numbers if isinstance(num, int) or isinstance(num, float)]

    def addiction(self, first_num, *numbers):
        numbers = self.string_catcher(numbers)
        if isinstance(first_num, int):
            result = first_num
            for num in numbers:
                result = result + num
            return result
        else:
            raise TypeError

    def subtraction(self, first_num, *numbers):
        numbers = self.string_catcher(numbers)
        if isinstance(first_num, int):
            result = first_num
            for num in numbers:
                result = result - num
            return result
        else:
            raise TypeError

    def multiply(self, first_num, *numbers):
        numbers = self.string_catcher(numbers)
        if isinstance(first_num, int):
            result = first_num
            for num in numbers:
                result = result * num
            return result
        else:
            raise TypeError

    def division(self, first_num, numbers):
        numbers = self.string_catcher(numbers)
        if isinstance(first_num, int):
            result = first_num
            for num in numbers:
                result = result / num
                if result % num == 0:  # Когда деление с остатком в консоль выводиться число с плавоющей точкой
                    result = int(result)
        else:
            raise Exception('The argument must be a integer')
        return result



class CommonCalculator(Calculator):
    pass
