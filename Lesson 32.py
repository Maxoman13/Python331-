# from cities import cities_list
import json
from dataclasses import dataclass
import pickle
import yaml

# @dataclass
# class City:
#     name: str
#     population: int
#
#     def __str__(self):
#         return f'Город {self.name}'
#
#
# city = City(name='Moscow', population=20000)
#
# print(city)
#
# with open('cities.pickle', 'wb') as f:
#     pickle.dump(city, f)
#
# with open('cities.pickle', 'rb') as f:
#     pickle_from_city = pickle.load(f)
#
# print(pickle_from_city)

json_string = """
[{
        "coords": {
            "lat": "52.65",
            "lon": "90.08333"
        },
        "district": "Сибирский",
        "name": "Абаза",
        "population": 14816,
        "subject": "Хакасия"
    },
    {
        "coords": {
            "lat": "53.71667",
            "lon": "91.41667"
        },
        "district": "Сибирский",
        "name": "Абакан",
        "population": 187239,
        "subject": "Хакасия"
    }]
"""

cities = json.loads(json_string)
print(type(cities))
print(cities)

yaml_string = yaml.dump(cities, allow_unicode=True)

print(type(yaml_string))
print(yaml_string)

with open('cities2.yaml', 'w') as yaml_file:
    yaml.dump(cities, yaml_file, allow_unicode=True)