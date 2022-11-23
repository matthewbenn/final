class Students:
    
    def __init__(self,student_name, student_id, gpa, expected_grade, status):
        self.__student_name = student_name
        self.__student_id = student_id
        self.__gpa = gpa
        self.__expected_grade = expected_grade
        self.__status = status


    def set_gpa(self, gpa):
        self.__gpa = gpa

    def set_expected_grade(self, expected_grade):
        self.__expected_grade = expected_grade


    def get_student_name(self):
        return self.__student_name

    def get_student_id(self):
        return self.__student_id

    def get_gpa(self):
        return self.__gpa

    def get_expected_grade(self):
        return self.__expected_grade

    def get_status(self):
        return self.__status

    def __str__(self):
        return f'Student Name: {self.__student_name}\n' + \
               f'Student ID: {self.__student_id}\n' + \
               f'Student GPA: {self.__gpa}\n' + \
               f'Expected Grade: {self.__expected_grade}\n' +\
               f'Enrollment Status: {self.__status}\n'

