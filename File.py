import os
fo = open("/home/karthik/Documents/word_count.txt","r+a+")
fo.write("I am ")
str = fo.read(10)
print str
position = fo.tell();
print "Current file position : ", position
print "Read is: ",str
print "File Name is: ",fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace
print os.getcwd()
fo.close()