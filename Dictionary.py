'''
A dictionary is a data type similar to arrays, but works with keys and values instead
 of indexes. Each value stored in a dictionary can be accessed using a key, which is 
 any type of object (a string, a number, a list, etc.) instead of using its index to 
 address it.
'''
phonebook = {};
phonebook["John"] = 989
phonebook["Jerry"] = 612
phonebook["Matt"] = 712

for name,number in phonebook.iteritems():
    print "%s --> %s" %(name,number)

# Alternative way of dictionary initialization    
phonebook1 = {
              "John":989,
              "Jerry":612,
              "Matt":712
              }

print
for name,number in phonebook1.iteritems():
    print "%s --> %s" %(name,number)
    
#To remove a specified index, use either one of the following notations:
del phonebook["John"]  # or phonebook.pop("John")

print
'''
Add "Jake" to the phonebook with the phone number 938273443, 
and remove Jill from the phonebook.
'''
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# write your code here
del phonebook["Jill"]
phonebook["Jake"] = 938273443
# or can be added by below syntax
'''
phonebook = {
          "Jake:938273443"
         }
'''

# testing code
if "Jake" in phonebook:
    print "Jake is listed in the phonebook."
if "Jill" not in phonebook:
    print "Jill is not listed in the phonebook."
    
for name,number in phonebook.iteritems():
    print "%s --> %s" %(name,number)