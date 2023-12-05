class BigMatryoshka:
    def __init__(self):
        self.size = 'Big'

    def open(self):
        print("Opening the big matryoshka")


class MediumMatryoshka(BigMatryoshka):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def open(self):
        print("Opening the medium matryoshka")
        super().open()

    def display_info(self):
        print(f"Opening the medium {self.color} matryoshka")


class SmallMatryoshka(MediumMatryoshka):
    def __init__(self, color):
        super().__init__(color)
        self.size = 'small'

    def open(self):
        super().open()
        print("Opening the small matryoshka")


user = SmallMatryoshka('red')
user.open()