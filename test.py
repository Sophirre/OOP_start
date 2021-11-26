def type_checker(num) -> float:
    if not isinstance(num, float):
        try:
            num = float(num)
        except:
            raise TypeError
    return num


def string_catcher(*numbers) -> list:
    return [num for num in numbers if isinstance(num, int) or isinstance(num, float)]


if __name__ == '__main__':
    tup = type_checker(23)
    print(tup)
    print(25 + 24.5)
