
class Employee:
    'Common base class for all employees'
    empCount = 0
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def getCount(self):
        print "Employee count: %d"%Employee.empCount
        
    def PrintDetails(self):
        print "Name: %s" %self.name, " Salary: %s" %self.salary
   
emp1 = Employee("KK", 2000)
emp2 = Employee("Vee", 3000)
emp1.PrintDetails();
emp2.PrintDetails();
print "Total Employees is: %d"%Employee.empCount
emp1.getCount()
print hasattr(emp1, 'salary')
print getattr(emp1, 'salary') 
setattr(emp1, 'age', 8)
print getattr(emp1,'age')
delattr(emp1, 'age')

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__
    