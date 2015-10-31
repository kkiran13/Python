'''
We have a class defined for vehicles. Create two new vehicles called car1 and car2. 
Set car1 to be a red convertible worth $60,000 with a name of Fer, 
and car2 to be a blue van named Jump worth $10,000.
'''
# define the Vehicle class
class Vehicle:
    'This class is about vehicles'
    name = ""
    kind = ""
    color = ""
    value = 0
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.value = 60000
car1.color = "red"
car1.kind = "convertible"

car2 = Vehicle()
car2.name = "Jump"
car2.value = 10000
car2.color = "blue"
car2.kind = "van"
# test code
print car1.description()
print car2.description()
print "Documentation string of class is: "+Vehicle.__doc__
