class Password:
    def __init__(self):
        self.__min_name_len = 8
        self.__max_name_len = 20
        self.__password = None

    def __check_len_password(self, password: str) -> bool:
        return self.__min_name_len <= len(password) <= self.__max_name_len

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str) -> None:
        if not self.__check_len_password(password):
            raise ValueError(f'Пароль должен быть от {self.__min_name_len} до {self.__max_name_len} символов')
        self.__password = password

    @password.deleter
    def password(self) -> None:
        self.__password = 'Пароль не задан'

# user = User('Николай', 30)
# print(user.name)
# user.name = 'Никола'
# # user.name = 'Ник0_ла!!'
#
# print(user.name)
#
# del user.name
# print(user.name)


user = Password()

print(user)

del user

