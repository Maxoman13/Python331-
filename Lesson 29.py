from functools import total_ordering


@total_ordering
class City:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def __eq__(self, other):
        return self.population == other.population

    def __le__(self, other):
        return self.population <= other.population

    def __str__(self):
        return f'Город: {self.name}, Население: {self.population}'


user = City('Вологда', 500000)
user2 = City('Краснодар', 5000000)

print(f'{user} == {user2} - {user == user2}')
print(f'{user} < {user2} - {user < user2}')
print(f'{user} > {user2} - {user > user2}')