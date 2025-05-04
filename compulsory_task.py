class Course:
    # Class attributes shared by all Course objects
    name = "Fundamentals of Computer Science" 
    contact_website = "www.hyperiondev.com"

    # Method to display contact website details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)
    # Method to display the head office location
    def head_office_location(self):
        print("Head Office Location: Cape Town")

class OOPCourse(Course):#Subclass inheriting from the course
    # Constructor method to initialize instance attributes
    def __init__(self):
        self.description = "OOP Fundamentals" #Course description
        self.trainer = "Mr Anon A. Mouse" #Trainer Name

    # Method to display course description and trainer detailS
    def trainer_details(self):
        print(f"Course Description: {self.description}")
        print(f"Trainer: {self.trainer}")
        
    # Method to display the course ID
    def show_course_id(self):
        print("Course ID: #12345")

# Create an object of the subclass
course_1 = OOPCourse()

# Call the required methods
course_1.contact_details() #Create an object (instance) of the OOPCourse class
course_1.trainer_details() #Call method to display trainer details
course_1.show_course_id() #Call method to display course ID
course_1.head_office_location() # Call inherited method to display head office location