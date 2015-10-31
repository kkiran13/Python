astring = "Hello world!"
print "Length of string is %d"%len(astring)  #length of string
print astring.index("o")  #gives index of first occurence of 'o'
print astring.count("l") # counts number of l's (case sensitive) in string
print astring[1:4]   # gives substring from index 1 to index 3
print astring.upper()  #upper case
print astring.lower() # lower case
print astring.startswith("Hello") # check if string startswith
print astring.endswith("ld!") # check if string endswith

splitlist = astring.split(" ") ## splits string into list
for i in splitlist:
    print i


s = "Hey there! what should this string be?"

# Length should be 20
print "Length of s = %d" % len(s)

# First occurrence of "a" should be at index 8
print "The first occurrence of the letter a = %d" % s.index("a")

# Number of a's should be 2
print "a occurs %d times" % s.count("a")

# Slicing the string into bits
print "The first five characters are '%s'" % s[:5] # Start to 5
print "The next five characters are '%s'" % s[5:10] # 5 to 10
print "The twelfth character is '%s'" % s[12] # Just number 12

print "The last five characters are %s" % s[-5:] # 5th-from-last to end

# Convert everything to uppercase
print "String in uppercase: %s" % s.upper()

# Convert everything to lowercase
print "String in lowercase: %s" % s.lower()

# Check how a string starts
if s.startswith("Str"):
    print "String starts with 'Str'. Good!"

# Check how a string ends
if s.endswith("ome!"):
    print "String ends with 'ome!'. Good!"

# Split the string into three separate strings,
# each containing only a word
print "Split the words of the string: %s" % s.split(" ")