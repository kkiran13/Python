import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root","TESTDB" )
#("localhost","username","password","database_name" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
'''
firstname = "Karthik"
lastname = "Kiran"
age = 25
sex = 'M'
income = 1000
'''
# Prepare SQL query to INSERT a record into the database directly
#sql = """Insert into EMPLOYEE values ('Veena', 'Kadle', 20, 'M', 2000)"""

'''
#Insert from variables
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )"\
       %(firstname, lastname, age, sex, income)
       
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
'''       

# disconnect from server
db.close()