# edit the functions prototype and implementation
def foo(a, b, c, *args):
    return len(args)

def bar(a, b, c, **kwargs):
    return kwargs["magicnumber"] == 7

def fobar(a,b,c,**args):
    if(args.get("arg1")==5):
        print "arg1 matched"
    if(args.get("arg2")==6):
        print "arg2 matched"


# test code
if foo(1,2,3,4) == 1:
    print "Good."
if foo(1,2,3,4,5) == 2:
    print "Better."
if bar(1,2,3,magicnumber = 6) == False:
    print "Great."
if bar(1,2,3,magicnumber = 7) == True:
    print "Awesome!"

fobar(1,2,3,arg1=5,arg2=6)

def foo1(first, second, third, *therest):
    print "First: %s" % first
    print "Second: %s" % second
    print "Third: %s" % third
    print "And all the rest... %s" % list(therest)
    
foo1(1,2,3,4,5,6)