class Car:
    car_count = 0

    def __init__(self, make, model, year, color):
        Car.car_count += 1
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        print(f'{Car.car_count}: {color} {make} {model} {year} ')

    def change_color(self, c):
        self.color = c
        return f'Color was changed to {self.color}'


car1 = Car('Toyota', 'Corolla', 1999, 'black')  # Инстенцианирование
car2 = Car('Kia', 'Rio', 2020, 'red')
car3 = Car('Audi', 'TT', 2013, 'white')
car4 = Car('Range Rover', 'Evoque', 2021, 'grey')
