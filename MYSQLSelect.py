import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root","TESTDB" )
#("localhost","username","password","database_name" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

#sql = """insert into EMPLOYEE values ('Komal','Kiran',27,'F',1500)"""
#cursor.execute(sql)
#db.commit()
sql = "select * from EMPLOYEE"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
# Now print fetched result
        print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" \
             %(fname, lname, age, sex, income ) 
except:
    print "Error: unable to fetch data"
    
db.close()