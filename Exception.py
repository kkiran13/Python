def do_stuff_with_number(n):
    print n

the_list = (1, 2, 3, 4, 5)

for i in range(20):
    try:
        do_stuff_with_number(the_list[i])
    except IndexError: # Raised when accessing a non-existing index of a list
        do_stuff_with_number(0)
        
        
try:
   fh = open("/home/karthik/Documents/word_count.txt","w")
   fh.write("This is my test file for exception handling!!")
   
except IOError:
   print "Error: can\'t find file or read data"
   
else:
   print "Written content in the file successfully"
   fh.close()