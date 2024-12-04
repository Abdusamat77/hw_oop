"задание№1"
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    
    def average_grade(self):
        if self.grades:
            average = sum(self.grades) / len(self.grades)
            print(f"Студент - {self.name}, возраст - {self.age}, средний балл - {average}")

student = Student("улукбек", 20, [85, 90, 78, 92])
student2 = Student("Абдусамат", 17, [90, 70, 60, 80])
student.average_grade()
student2.average_grade()

"задание№2"
class Movie:
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
    
    def duration_category(self):
        if self.duration < 60:
            category = "короткий"
        elif 60 <= self.duration <= 120:
            category = "средний"
        else:
            category = "длинный"
        print(f"Фильм '{self.title}' {self.director} длится {self.duration} категория: {category}")


movie1 = Movie("футбол", "абдусамат", 45)
movie2 = Movie("волейбол", "улукбек", 90)
movie3 = Movie("баскетбол", "айбек", 130)

movie1.duration_category()
movie2.duration_category()
movie3.duration_category()