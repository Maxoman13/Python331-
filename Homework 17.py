class SmartHome:
    def __init__(self, name: str):
        self.name = name

    def switch_on(self):
        return f'{self.name} включено'

    def switch_off(self):
        return f'{self.name} выключено'

    def battery(self):
        return f'{self.name} в процессе работы'


user = SmartHome('Maksim house')
print(user.switch_on())
print(user.switch_off())
print(user.battery())


