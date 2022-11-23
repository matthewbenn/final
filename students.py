class Students:
    
    # The __init__ method initializes the attributes.

    def __init__(self,student_name, student_id, gpa, expected_grade, status):
        self.__student_name = student_name
        self.__student_id = student_id
        self.__gpa = gpa
        self.__expected_grade = expected_grade
        self.__status = status

##    # The set_manufact method accepts an argument for
##    # the phone's manufacturer.
##
##    def set_student_name(self, student_name):
##        self.__student_name = student_name
##
##    # The set_model method accpets an argument for
##    # the phone's model
##
##    def set_student_id(self, student_id):
##        self.__student_id = student_id
##
##    # The set_retail_price method accepts an argument
##    # for the phone's retail price.
##
##    def set_gpa(self, gpa):
##        self.__gpa = gpa
##
##    def set_expected_grade(self, expected_grade):
##        self.__expected_grade = expected_grade
##
##    def set_status(self, status):
##        self.__status = status
##
    # The get_manufact method returns the
    # phone's manufacturer.

    def get_student_name(self):
        return self.__student_name

    # The get_model method returns the
    # phone's model number.

    def get_student_id(self):
        return self.__student_id

    # The get_retail_price method returns the
    # phone's retail price.

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

