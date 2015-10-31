x = 1
if x==1:
	print x

mystring = "hello"
myfloat = 10.0
myint = 10

if isinstance(myfloat,float) and myfloat == 10.0:
	print myfloat
	
mylist = []
mylist.append(10)
mylist.append(20)
mylist.append(30)

for x in mylist:
	print x
	
print "hello"*2 # repeat strings

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers  #Join(Concat) lists

print all_numbers

print [1,2,3] * 3 #Repeat a list

print 7**2    # Square (Power)

name = "John"
age = 23
point = 1.345678

print "%s is %d years old! point is %f with precision is %.1f" %(name,age,point,point)

print "list is %s" %even_numbers

data = ("John", "Doe", 53.44)
format_string = "Hello"

print "%s %s %s. Your current balance is %.2f$."%(format_string,data[0],data[1],data[2])

list1 = ["John","Rick"]

na = "Joh"

if na in list1:
	print "true"
else:
	print "false"
	
x = [1,2,3]
y = x
print x == y # Prints out True
print x is y # Pr	ints out False


