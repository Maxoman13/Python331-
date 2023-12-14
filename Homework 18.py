import json
from typing import List, Dict


class JsonFile:

    def __init__(self, filepath: str):
        self.data = None
        self.filepath = filepath

    def read_file(self, as_dict=False) -> List[Dict] | List[List]:
        """
        Метод для чтения данных из JSON файла.
        Флаг as_dict работает аналогично как в классе CsvFileHandler.
        Должен быть реализован как метод экземпляра.
        :param as_dict: bool
        :param filepath: str
        :return: List[Dict] | List[List]
        """
        with open(self.filepath, 'r', encoding='utf-8') as file:
            self.data = json.load(file)
            return self.data


class Cities:

    def __init__(self, city_data):
        self.city_data = city_data
