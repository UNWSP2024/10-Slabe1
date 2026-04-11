# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.


class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title
    
    def print_data(self):
        print(self.name, self.id_number, self.department, self.job_title)
    

def main():
    susan = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    mark = Employee("Mark Jones", 39119, "IT", "Programmer")
    joy = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
    susan.print_data()
    mark.print_data()
    joy.print_data()
 
main()

