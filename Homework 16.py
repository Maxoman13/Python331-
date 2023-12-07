import csv
import json


class CsvFileHandler:

    @staticmethod
    def read_file(filepath, as_dict=False):
        with open(f'{filepath}', 'r', encoding='windows-1251', newline='') as f:
            file = csv.reader(f, delimiter=';')
            file_list = [row for row in file]
            print(file_list)

    @staticmethod
    def write_file(filepath, data, as_dict=False):
        with open(f'{filepath}', 'w', encoding='windows-1251', newline='') as f:
            file = csv.writer(f, delimiter=';')
            file.writerow(data)
            return file

    @staticmethod
    def append_file(filepath, data, as_dict=False):
        with open(f'{filepath}', 'a', encoding='windows-1251', newline='') as f:
            file = csv.writer(f, delimiter=';')
            file.writerow(data)
            return file
#
#
# user_file = CsvFileHandler()
# user_file.write_file('C:/Users/User/Desktop/Python/Python331-/Лист Microsoft Excel.csv', 'Море')
# user_file.append_file('C:/Users/User/Desktop/Python/Python331-/Лист Microsoft Excel.csv', 'Жара')
# user_file.read_file('C:/Users/User/Desktop/Python/Python331-/Лист Microsoft Excel.csv')


# class JsonFileHandler:
#
#     @staticmethod
#     def read_file(filepath, as_dict=False):
#         with open(f'{filepath}', 'r', encoding='UTF-8', newline='') as f:
#             file = json.load(f)
#             print(file)
#
#     @staticmethod
#     def write_file(filepath, data, as_dict=False):
#         with open(f'{filepath}', 'w', encoding='UTF-8', newline='') as f:
#             json.dump(list(data), f, ensure_ascii=False, indent=4)
#
#     @staticmethod
#     def append_file(filepath, data, as_dict=False):
#         try:
#             with open(f'{filepath}', 'a', encoding='UTF-8', newline='') as f:
#                 json.dump(list(data), f, ensure_ascii=False, indent=4)
#         except TypeError:
#             print('В JSON нельзя записывать')
#
#
# user_file = JsonFileHandler()
# user_file.write_file('C:/Users/User/Desktop/Python/Python331-/привет.json', 'Море')
# user_file.append_file('C:/Users/User/Desktop/Python/Python331-/привет.json', 'Жара')
# user_file.read_file('C:/Users/User/Desktop/Python/Python331-/привет.json')


class TxtFileHandler:

    @staticmethod
    def read_file(filepath):
        with open(f'{filepath}', 'r', encoding='UTF-8', newline='') as f:
            file = f.read()
            print(file)

    @staticmethod
    def write_file(filepath, data):
        with open(f'{filepath}', 'w', encoding='UTF-8', newline='') as f:
            file = f.write(data+'\n')
            return file

    @staticmethod
    def append_file(filepath, data):
        with open(f'{filepath}', 'a', encoding='UTF-8', newline='') as f:
            file = f.write(data+'\n')
            return file
#
#
# user_file = TxtFileHandler()
# user_file.write_file('C:/Users/User/Desktop/Python/Python331-/привет.txt', 'Море')
# user_file.append_file('C:/Users/User/Desktop/Python/Python331-/привет.txt', 'Жара')
# user_file.read_file('C:/Users/User/Desktop/Python/Python331-/привет.txt')
