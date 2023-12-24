import json
from typing import List, Dict, Set


class JsonFile:
    """
    Класс для работы с Json.
    read_file() - чтение
    write_file() - запись
    """
    def __init__(self, file_name: str):
        self.file_name = file_name

    def read_file(self):
        """
        Метод для чтения данных из JSON файла.
        :return: горорода из JSON файла.
        """
        with open(self.file_name, 'r', encoding='utf-8') as file:
            data_file = json.load(file)
        return data_file

    @staticmethod
    def write_file(data_file: str):
        """
        Метод для записи данных в JSON файла.
        :param data_file: данные для записи
        :return: None
        """
        with open("result.json", 'w', encoding='utf-8') as file:
            json.dump(data_file, file, ensure_ascii=False, indent=4)


class Cities:
    """
    Класс для получения данных о городах из JSON-файла.
    """
    def __init__(self, city_data):
        self.city_data = city_data
        self.names_set = self.__get_set()

    def __get_set(self):
        """
        Получение сета городов
        :return: сет городов
        """
        names_set = set()
        for city in self.city_data:
            names_set.add(city['name'])
        return names_set