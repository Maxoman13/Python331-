
class Alert:
    def __init__(self):
        self.message = 'Вам отправлено срочное уведомление'

    def send_message(self):
        print('Вам отправлено срочное уведомление')


class AddWifi:

    def __init__(self, name_wifi, password):
        self.name_wifi = 'Kvartira30'
        self.password = 'password'

    def wifi_connect(self):
        return 'Kvartira30', 'password'


class TimeTable:
    def __init__(self, worktime: dict):
        self.worktime = worktime

    def set_time(self):
        return f'{self.worktime}'


class SmartHome:
    def __init__(self, name: str):
        self.name = name

    def switch_on(self):
        return f'Умный дом в {self.name} включен'

    def switch_off(self):
        return f'Умный дом в {self.name} выключен'

    def condition(self):
        return f'Умный дом в {self.name} в процессе работы'


class SmartLight(SmartHome):
    def __init__(self, name: str, bright: int, condition: bool):
        super().__init__(name)
        self.bright = bright
        self.condition = condition

    def switch_on(self):
        super().switch_on()
        return f'Свет в {self.name} включен'

    def switch_off(self):
        super().switch_off()
        return f'Свет в {self.name} выключен'

    def light_bright(self):
        if self.condition is True:
            return f'Уровень яркости {self.bright}'
        else:
            return f'Лампочка в {self.name} не работает, включите её'


class SmokeScreen(SmartHome, AddWifi):
    def __init__(self, name: str, condition: int):
        super().__init__(name)
        self.condition = condition

    def switch_on(self):
        super().switch_on()
        return f'Датчик дыма в {self.name} включен'

    def switch_off(self):
        super().switch_off()
        return f'Датчик дыма в {self.name} выключено'

    def smoke_lvl(self):
        if self.condition is True:
            return f'В {self.name} задымление. Проверьте причину'
        else:
            return f'В {self.name} всё хорошо'


class SmartWet(SmartHome, Alert):
    def __init__(self, name: str, wet: int, condition: bool):
        super().__init__(name)
        self.wet = wet
        self.condition = condition

    def switch_on(self):
        super().switch_on()
        return f'Проверка уровня влажности в {self.name} включена'

    def switch_off(self):
        super().switch_off()
        return f'Проверка уровня влажности в {self.name} выключена'

    def wet_lvl(self):
        if self.condition is True:
            return f'Уровень влажности {self.wet}'
        else:
            return f'Уровень влажности в {self.name} не работает, включите его'


user2 = SmartHome('Dragon')
print(user2.switch_on())
print(user2.switch_off())

user = SmartLight('House', 70, True)
print(user.switch_on())
print(user.switch_off())
print(user.light_bright())

user3 = SmokeScreen('House', True)
print(user3.switch_on())
print(user3.switch_off())
print(user3.wifi_connect())

print(user3.__dict__)