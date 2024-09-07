from datetime import datetime

class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []
        self._grades = {}  

    def enroll(self, course, grade=None):
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
            if grade is not None:
                self._grades[enrollment] = grade
        else:
            raise TypeError("course must be an instance of Course")

    def get_enrollments(self):
        return self._enrollments.copy()

    def course_count(self):
        return len(self._enrollments)

    def aggregate_average_grade(self):
        total_grades = sum(self._grades.values())
        num_courses = len(self._grades)
        return total_grades / num_courses if num_courses > 0 else 0


class Course:
    def __init__(self, title):
        self.title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        if isinstance(enrollment, Enrollment):
            self._enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of Enrollment")

    def get_enrollments(self):
        return self._enrollments.copy()


class Enrollment:
    all = []
    
    def __init__(self, student, course):
        if isinstance(student, Student) and isinstance(course, Course):
            self.student = student
            self.course = course
            self._enrollment_date = datetime.now()
            type(self).all.append(self)
        else:
            raise TypeError("Invalid types for student and/or course")

    def get_enrollment_date(self):
        return self._enrollment_date
    
    @classmethod
    def aggregate_enrollments_per_day(cls):
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count



math = Course("Math")
Computer_science = Course("Computer science")


Sia = Student("Sia")
Tim = Student("Tim")


Sia.enroll(math, grade=80)
Sia.enroll(Computer_science, grade=70)
Tim.enroll(math, grade=88)


print(f"Sia is enrolled in {Sia.course_count()} courses.")  


print(f"Sia's average grade is {Sia.aggregate_average_grade()}") 

enrollments_per_day = Enrollment.aggregate_enrollments_per_day()
print(f"Enrollments per day: {enrollments_per_day}")
