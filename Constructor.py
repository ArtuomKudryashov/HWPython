class Employee:
    'Common base class for all employees'
    empCount = 0  # will count our employee

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    @staticmethod
    def displayCount():
        print("Total Employee %d" % Employee.empCount)
        # %d is the format specifier used to print integers or numbers

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)  # 1-st object
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)  # 2-d object

emp1.displayEmployee()
emp2.displayEmployee()

# print("Total Employee %d" % Employee.empCount)
Employee.displayCount()
