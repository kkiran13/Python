import smtplib

sender = 'karthik.kiran23@gmail.com'
receivers = 'veena.kadle@gmail.com'

message = """From: From Person <sender>
To: To Person <receivers>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)         
    print "Successfully sent email"
except:
    print "Error: unable to send email"