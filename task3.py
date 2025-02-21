# Создайте класс Student, который имеет:

# Атрибуты name, age и grades (список оценок).

# Метод add_grade(grade), который добавляет новую оценку
# в список.

# Метод average_grade, который возвращает средний балл студента.


class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.__grades = grades

    def add_grade(self, grade):
        self.__grades.append(grade)

    def average_grade(self):
        return sum(self.__grades)/len(self.__grades)


if __name__ == "__main__":
    st = Student("test_stud", 11,[5,4])
    print(st.average_grade())
    st.add_grade(2)
    print(st.average_grade())
