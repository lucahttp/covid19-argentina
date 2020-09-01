# https://stackoverflow.com/questions/4408714/execute-sql-file-with-python-mysqldb
#from os import system
#USERNAME = "root"
#PASSWORD = "root"
#DBNAME = "mydatabase"
#HOST = "localhost"
#PORT = 3306
#FILE = "dump.sql"
#command = """mysql -u %s -p"%s" --host %s --port %s %s < %s""" %(USERNAME, PASSWORD, HOST, PORT, DBNAME, FILE)

#command = "c:/xampp/mysql/bin/mysql.exe --user=root --password=''  -e 'show databases;'"
#system(command)
# https://www.cyberciti.biz/faq/mysql-command-to-show-list-of-databases-on-server/
# .\mysql.exe -u root -p '' -e 'show databases;'
# .\mysql.exe -u your-user-name -p'Your-password'
# .\mysql.exe --user=root --password=""  -e 'show databases;'
# C:\xampp\mysql\bin\mysql.exe --user=root --password=""  -e 'show databases;'

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="test"
)
if mydb.cursor:
  print("done")


