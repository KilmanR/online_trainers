class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students

    @staticmethod
    def validate_score(score):
        return isinstance(score, (int, float)) and 1 <= score <= 10

    def __str__(self):
        return f"Курс: {self.name}, Макс. студентов: {self.max_students}"


class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, score):
        if Course.validate_score(score):
            self.grades.append(score)
            return None
        return 'Ошибка: оценка от 1 до 10'

    def get_average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Студент: {self.name}, Средний балл: {self.get_average():.1f}"


class Group:
    def __init__(self, course, students=None):
        self.course = course
        self.students = students if students is not None else []

    @classmethod
    def from_dict(cls, course_name, max_students, student_names):
        course_obj = Course(course_name, max_students)
        students_list = [Student(name) for name in student_names]
        return cls(course_obj, students_list)

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
            return None
        return 'Ошибка: передан не студент'

    def get_top_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.get_average())

    def get_group_average(self):
        if not self.students:
            return 0.0
        return sum(s.get_average() for s in self.students) / len(self.students)

    def __str__(self):
        avg = self.get_group_average()
        return f"Группа [{self.course.name}] | Студентов: {len(self.students)} | Средний балл группы: {avg:.1f}"


# ================= ТЕСТЫ =================
print('\n=== ЗАДАНИЕ 3.1: Проверка ===')

course = Course("Python Basics", 30)
print(course)

s1 = Student("Алиса")
s2 = Student("Борис")
s3 = Student("Вика")

s1.add_grade(9); s1.add_grade(10); s1.add_grade(8)
s2.add_grade(7); s2.add_grade(7); s2.add_grade(6)
s3.add_grade(10); s3.add_grade(10)

print(s1)
print(s2.add_grade(15))  # Ошибка: оценка от 1 до 10

group = Group(course, [s1, s2, s3])
print(group)
print(f"Лучший студент: {group.get_top_student().name}")
print(f"Средний балл группы: {group.get_group_average():.1f}")

group2 = Group.from_dict("Git Intro", 20, ["Олег", "Мария"])
print(group2)