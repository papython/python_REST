#!/usr/bin/python

import MySQLdb
import random
import string

# Open database connection
db = MySQLdb.connect("localhost","appuser","test","appdb" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print "Database version : %s " % data

x = 0
while x < 100:
 topic = ''.join([random.choice(string.digits) for n in xrange(6)])
 content = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(500)])

# Prepare SQL query to INSERT a record into the database.
 sql = "INSERT INTO messages (client_id, topic, content) VALUES (" + str(random.randint(1,100)) + "," + topic + "," + "\"" + content + "\")"
 print sql
 exit
 try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
   print "done commit"
 except MySQLdb.Error, e:
   try:
    print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
   except IndexError:
    print "MySQL Error: %s" % str(e)
   except TypeError, e:
    print(e)
   except ValueError, e:
    print(e)
   finally:
   # Rollback in case there is any error
    db.rollback()
    print "failed"
 x = x + 1

# disconnect from server
db.close()
