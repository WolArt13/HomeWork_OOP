class Student:
    """Модель студента"""
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lr(self, lecturer, course, grade):
        """Функция, реализующая возможность оценивать лектора"""
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def average_rating(self):
        """Функция для вычисления средней оценки по предметам"""
        if self.grades:
            grades_count = 0
            for i in self.grades:
                grades_count += len(self.grades[i])
            average_rating = sum(map(sum, self.grades.values())) / grades_count
            return average_rating
        else: return 0

    def __str__(self):
        """Переопределение __str__ для вывода в print(student) в нужном формате"""

        courses_in_progress_str = ", ".join(self.courses_in_progress)
        finished_courses_str = ", ".join(self.finished_courses)
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {round(self.average_rating(), 2)}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_str}\n' \
              f'Завершенные курсы: {finished_courses_str}'
        return res
    
    def __lt__(self, other):
        """Переопределение функции сравнения, 
        для корректного вывода результата сравнения одного студента с другим"""
        if not isinstance(other, Student):
            print('Не верное сравнение')
            return
        return self.average_rating() < other.average_rating()
       
class Mentor:
    """Родительский класс Ментора"""
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    """Дочерний класс Лектора"""
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rating(self):
        """Функция для опеределения среднего рейтинга"""
        if self.grades:
            grades_count = 0
            for i in self.grades:
                grades_count += len(self.grades[i])
            average_rating = sum(map(sum, self.grades.values())) / grades_count
            return average_rating
        else: return 0

    def __str__(self):
        """Переопределение __str__ для вывода в print(lecturer) в нужном формате"""
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.average_rating(), 2)}'
        return res
    
    def __lt__(self, other):
        """Переопределение функции сравнения, 
        для корректного вывода результата сравнения одного студента с другим"""
        if not isinstance(other, Lecturer):
            print('Не верное сравнение')
            return
        return self.average_rating() < other.average_rating()

class Reviewer(Mentor):
    """Дочерний класс Проверяющего"""
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        """Функция для оценки студента"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        """Переопределение __str__ для вывода в print(reviewer) в нужном формате"""
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
 
# Создаем лекторов и закрепляем их за курсом
lecturer_1 = Lecturer('Павел', 'Бастрыкин')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Юрий', 'Дефолтов')
lecturer_2.courses_attached += ['Java']

lecturer_3 = Lecturer('Урнульд', 'Швирсникер')
lecturer_3.courses_attached += ['Python']

# Создаем проверяющих и закрепляем их за курсом
reviewer_1 = Reviewer('Сам', 'Бадди')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']

reviewer_2 = Reviewer('Рик', 'Санчес')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Java']

# Создаем студентов и определяем для них изучаемые и завершенные курсы
student_1 = Student('Морти', 'Санчес')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Технический английский']

student_2 = Student('Джонни', 'Синс')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Вася', 'Пупкин')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Гейм-дизайнер']

# Выставляем оценки лекторам за лекции
student_1.rate_lr(lecturer_1, 'Python', 7)
student_1.rate_lr(lecturer_1, 'Python', 10)
student_1.rate_lr(lecturer_1, 'Python', 9)

student_1.rate_lr(lecturer_2, 'Python', 6)
student_1.rate_lr(lecturer_2, 'Python', 4)
student_1.rate_lr(lecturer_2, 'Python', 7)

student_1.rate_lr(lecturer_1, 'Python', 10)
student_1.rate_lr(lecturer_1, 'Python', 10)
student_1.rate_lr(lecturer_1, 'Python', 10)

student_2.rate_lr(lecturer_2, 'Java', 9)
student_2.rate_lr(lecturer_2, 'Java', 10)
student_2.rate_lr(lecturer_2, 'Java', 10)

student_3.rate_lr(lecturer_3, 'Python', 3)
student_3.rate_lr(lecturer_3, 'Python', 5)
student_3.rate_lr(lecturer_3, 'Python', 4)

# Выставляем оценки студентам за домашние задания
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_2.rate_hw(student_2, 'Java', 10)
reviewer_2.rate_hw(student_2, 'Java', 9)
reviewer_2.rate_hw(student_2, 'Java', 8)

reviewer_2.rate_hw(student_3, 'Python', 8)
reviewer_2.rate_hw(student_3, 'Python', 9)
reviewer_2.rate_hw(student_3, 'Python', 2)
reviewer_2.rate_hw(student_3, 'Python', 8)
reviewer_2.rate_hw(student_3, 'Python', 5)
reviewer_2.rate_hw(student_3, 'Python', 5)

# Характеристики созданных и оцененых студентов
print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()
print()

# Характеристики созданных и оцененых лекторов
print(f'Перечень лекторов:\n\n{lecturer_1}\n\n{lecturer_2}\n\n{lecturer_3}')
print()
print()

# Результат сравнения студентов по средним оценкам за домашние задания
print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')
print()

# Результат сравнения лекторов по средним оценкам за лекции
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{lecturer_1.name} {lecturer_1.surname} < {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 > lecturer_2}')
print()
print()

def students_average_rating(students_list, course_name):
    """Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
    в качестве аргументов принимает список студентов и название курса"""
    #Общий список оценок студентов по конкретному курсу
    overall_grades = []
    #Отбираем оценки по курсу
    for student in students_list:
        for course, grades in student.grades.items():
            if course == course_name:
                overall_grades += grades
    #Находим средний балл среди оценок всех студентов
    sum_all = 0
    count_all = len(overall_grades)
    for grade in overall_grades:
        sum_all += grade
    average_rating_for_all = sum_all / count_all
    return average_rating_for_all

def lecturers_average_rating(lecturers_list, course_name):
    """Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
    в качестве аргумента принимает список лекторов и название курса"""
    #Общий список оценок лекторов по конкретному курсу
    overall_grades = []
    #Отбираем оценки по курсу
    for lecturer in lecturers_list:
        for course, grades in lecturer.grades.items():
            if course == course_name:
                overall_grades += grades
    #Находим средний балл среди оценок всех лекторов
    sum_all = 0
    count_all = len(overall_grades)
    for grade in overall_grades:
        sum_all += grade
    average_rating_for_all = sum_all / count_all
    return average_rating_for_all
    
#Создаем списки студентов
students = [student_1, student_2, student_3]

#Узнаем средний бал студентов в рамках конкретного курса
print(f'Средний балл у студентов по курсу Python: {round(students_average_rating(students, 'Python'), 2)}')
print()

print(f'Средний балл у студентов по курсу Java: {round(students_average_rating(students, 'Java'), 2)}')
print()
print()

#Создаем списки лекторов
lecturers = [lecturer_1, lecturer_2, lecturer_3]

#Узнаем средний бал лекторов в рамках конкретного курса
print(f'Средний балл у лекторов по курсу Python: {round(lecturers_average_rating(lecturers, 'Python'), 2)}')
print()

print(f'Средний балл у лекторов по курсу Java: {round(lecturers_average_rating(lecturers, 'Java'), 2)}')
print()