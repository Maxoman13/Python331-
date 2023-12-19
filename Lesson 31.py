from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


person = Person('Maksim', 30)
person2 = Person('Ivan', 30)

print(person)
print(person2)