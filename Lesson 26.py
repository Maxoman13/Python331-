class Password:
    def __init__(self):
        self.__min_name_len = 8
        self.__max_name_len = 20
        self.__password = None

    def __check_len_password(self, new_password: str) -> bool:
        return self.__min_name_len <= len(new_password) <= self.__max_name_len

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, new_password: str) -> None:
        if not self.__check_len_password(new_password):
            raise ValueError(f'Пароль должен быть от {self.__min_name_len} до {self.__max_name_len} символов')
        self.__password = new_password

    @password.deleter
    def password(self) -> None:
        self.__password = 'Пароль не задан'


user = Password()

print(user.password)

user.password = 'Пароль12334'

del user.password

print(user.password)

