class BigMatryoshka:
    def __init__(self):
        self.size = 'Big'

    def open(self):
        print(f"Opening the big matryoshka")


class MediumMatryoshka(BigMatryoshka):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def open(self):
        print(f"Opening the medium matryoshka")
        super().open()

    def display_info(self):
        print(f"Opening the {self.size} {self.color} matryoshka")


user = MediumMatryoshka('Red')
user.open()