# Создайте класс Triangle, который имеет:

# Атрибуты a, b и c для хранения длины сторон.

# Метод is_valid, который проверяет, можно ли из этих
# сторон составить треугольник (сумма любых двух сторон
# должна быть больше третьей).

# Метод perimeter, который возвращает периметр треугольника,
# если он существует, или выводит сообщение "Треугольник недопустим".

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self):
        conditions = [
            self.a + self.b > self.c,
            self.b + self.c > self.a,
            self.c + self.a > self.b
        ]
        return all(conditions)

    def perimeter(self):
        return self.a + self.b + self.c


if __name__ == "__main__":
    tr1 = Triangle(1, 2, 3)
    print(tr1.is_valid())
    tr2 = Triangle(2, 3, 2)
    print(tr2.is_valid(), tr2.perimeter())

