from dataclasses import dataclass


@dataclass(order=True)
class Book:
    name: str
    author: str
    year: int


book1 = Book('Гарри Поттер', 'Джоан Роулинг', 1998)
book2 = Book('Евгений Онегин', 'Александр Пушкин', 1721)
book3 = Book('Игра Престолов', 'Джордж Мартин', 1999)

books = [book1, book2, book3]
books.sort()
print(books)
print(sorted(books, key=lambda book: book.year))
