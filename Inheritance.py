class Parent:
    ParentAttr = 0
    def __int__(self):
        print "Calling parent Constructor"
        
    def parentMethod(self):
        print 'Calling parent method' 
    
    def setAttr(self,attr):
        Parent.ParentAttr = attr 
       
    def getAttr(self):
        print "Parent Attr is: ",Parent.ParentAttr
    

class Child(Parent):
    def __init__(self):
        print "Calling child constructor"

    def childMethod(self):
        print 'Calling child method'
      
      
c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(300)
c.getAttr()
