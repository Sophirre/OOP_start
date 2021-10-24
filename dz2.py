class Car:
    MAKE = 'Mersedes'
    model = 'S-Class W222'
    amg_pack = False
    color = 'black'
    gearbox = 'default'
    alowed_gears = 6
    gear = 0
    brake = 'default'

    def set_amg(self):
        self.amg_pack = True
        self.model = f'{self.model} AMG'
        self.gearbox = 'AMG gear'
        return 'AMG pack was succssesfully instaled'

    def change_color(self, c):
        self.color = c
        return f'Color was changed to {self.color}'

    def start_engine(self):
        return f'{self.MAKE} {self.model} was started'

    def stop_engine(self):
        return '...'

    def switch_gear(self):
        if self.gear <= self.alowed_gears - 1:
            self.gear += 1
        else:
            self.gear = 1
        return self.gear

    def push_brake(self):
        return f'{self.MAKE} {self.model} turn slowly'


car1 = Car()