'''
An object's attributes may or may not be visible outside the class definition. 
You need to name attributes with a double underscore prefix, and those attributes 
then are not be directly visible to outsiders.
'''

class JustCounter:
    __secretCount = 0 #Data Hiding
  
    def count(self):
        self.__secretCount += 1
        print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
print counter._JustCounter__secretCount
#Python protects those members by internally changing the name to include the class 
#name. You can access such attributes as object._className__attrName.

#print counter.__secretCount gives error