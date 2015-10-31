import MySQLdb

db = MySQLdb.Connect("localhost","root","root","TESTDB")
cursor = db.cursor()

# Drop table if exists
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

#Read CSV Line by Line and insert into table
for line in open("/home/karthik/Documents/Python/samplecsv.csv"):
        row = line.split(",")
        sql = "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) \
        VALUES ('%s', '%s', '%d', '%c', '%.2f' )"\
        %(row[0], row[1], int(row[2]), row[3], float(row[4]))
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

f = open("/home/karthik/Documents/Python/WriteFile.txt",'a')
sql = "select * from EMPLOYEE"
cursor.execute(sql)
results = cursor.fetchall()

for row in results:
    f.write(row[0]+';'+row[1]+';'+str(row[2])+';'+row[3]+';'+str(row[4])+'\n')

f.close()
  
db.close()