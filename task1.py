# Создайте класс Book, который имеет:

# Атрибуты title, author и year.
# Метод get_info, который возвращает строку с информацией о книге в формате:
# "Название: [title], Автор: [author], Год издания: [year]".


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self. author = author
        self. year = year

    def get_info(self):
        return (f"Название: {self.title}, "
                f"Автор: {self.author}, Год издания: {self.year}")


if __name__ == "__main__":
    book = Book("Старик и море", "Эрих Мария Ремарк", 1952)
    print(book.get_info())

