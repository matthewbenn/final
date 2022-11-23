import students
import pickle


LOOKUP = 1
ADD = 2
CHANGEGPA = 3
CHANGEEXP = 4
TABPRINT = 5
QUITNSAVE = 6
MAKEFIVE = 7

STUDENTFILE = 'students.dat'

def load_students():
    try:
      # Open the contacts.dat file.
      input_file = open(STUDENTFILE, 'rb')

      # Unpickle the dictionary.
      student_dictionary = pickle.load(input_file)

      # Close the phone_inventory.dat file.
      input_file.close()
    except IOError:
      # Could not open the file, so create
      # an empty dictionary.
      student_dictionary = {}

    # Return the dictionary.
    return student_dictionary

def main():
    my_students = load_students()
    choice = 0

    while choice != QUITNSAVE:
        
        choice = display_menu()
        
        if choice == LOOKUP:
            lookup_gpa(my_students)
            
        elif choice == ADD:
            add_student(my_students)
            
        elif choice == CHANGEGPA:
            change_gpa(my_students)
        
        elif choice == CHANGEEXP:
            change_expected_grade(my_students)
        
        elif choice == TABPRINT:
            print_students(my_students)
            
        elif choice == MAKEFIVE:
            make_five(my_students)

            
    save_students(my_students)

            
        
def display_menu():
    print('1) Look up a student\'s GPA.')
    print('2) Add a student to the list.')
    print('3) Change a student\'s GPA.')
    print('4) Change a student\'s expected grade.')
    print('5) Print a tabulated list of students.')
    print('6) Quit this program and save to disk.')
    print()
    try:
        choice = int(input('Enter a menu selection: '))
        while choice < LOOKUP or choice > MAKEFIVE:
            choice = int(input('Invalid, enter again: '))
    except ValueError:
        choice = int(input('Invalid, enter again: '))
    return choice
            

def add_student(my_students):
    stu_name = input('Enter the student\'s name: ')
    stu_id = input('Enter the student\'s ID number: ')
    stu_g = float(input('Enter the studnet\'s GPA: '))
    stu_ep = float(input('Enter their expected grade: '))
    stu_stat = str(input('Enter their status (FT/PT)'))
    print()

    record = students.Students(stu_name, stu_id, stu_g, stu_ep, stu_stat)

    if stu_name not in my_students:
        my_students[stu_name] = record
        print('----------')
        print('Success!')
        print('----------')
    else:
        print('----------')
        print('Already exists!')
        print('----------')


def lookup_gpa(my_students):
    name = input('Enter the student\'s name: ')
       
    if name in my_students:
        print('----------')
        print(my_students[name].get_student_name())
        print(my_students[name].get_gpa())
        print('----------')
        
    else:
        print('----------')
        print('Student not found!')
        print('----------')
        

def lookup_student(my_students):
    student = input('What is the student\'s name? ')

    print(my_students.get(student, 'Can\'t find that student.'))


def change_gpa(my_students):
    name = input('Enter the student\'s name: ')

    if name in my_students:
        gpa = input('Enter their new GPA: ')
        my_students[name].set_gpa(gpa)
        print('----------')
        print('Updated!')
        print(my_students[name].get_student_name())
        print(my_students[name].get_gpa())
        print('----------')
    else:
        print('----------')
        print('Not found!')
        print('----------')


def change_expected_grade(my_students):
    name = input('Enter the student\'s name: ')

    if name in my_students:
        exp = input('Enter their new expected grade: ')
        my_students[name].set_expected_grade(exp)
        print('----------')
        print('Updated!')
        print(my_students[name].get_student_name())
        print(my_students[name].get_expected_grade())
        print('----------')
    else:
        print('----------')
        print('Not found!')
        print('----------')



def save_students(my_students):
    output_file = open(STUDENTFILE,'wb')

    pickle.dump(my_students, output_file)
    output_file.close()



    
def print_students(my_students):
    for name in my_students:
        print('----------')
        print(f'{my_students[name].get_student_name()}')
##        print(my_students.get(name,'Student not found!'))
        print('----------')

    
def make_five(my_students):

    print('Entering data for five students.')
    for count in range(1,3):
        print('Student number ' + str(count) + ':')
##        stu_name = input('Enter the student\'s name: ')
##        stu_id = input('Enter the student\'s ID number: ')
##        stu_g = float(input('Enter the studnet\'s GPA: '))
##        stu_ep = float(input('Enter their expected grade: '))
##        stu_stat = str(input('Enter their status (FT/PT)'))
        print()

        record = students.Students(stu_name, stu_id, stu_g, stu_ep, stu_stat)

        if stu_name not in my_students:
            my_students[stu_name] = record
            print('Success!')
        else:
            print('Already exists!')

main()
