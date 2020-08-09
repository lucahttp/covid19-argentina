import os, time, datetime
from datetime import timedelta

import pandas as pd 
import sqlite3


# check if db exist

    # check if the expiration date has passed

        # do
            # delete csv
            # delete db
            # download csv
            # create db
        
        # pass

    # do
        # download csv
        # create db




#get file date
def getLastUpdateOfFile(file):
    print(file)
    created = os.path.getctime(file)
    return created



#add time to a specific date to create the due date
def setPassDay(mydate):
    
    print("incoming date "+ str(mydate))

    theNextDay = mydate + timedelta(days=1)
    theNextDay = theNextDay.replace(hour=20, minute=00, second=00, microsecond=00) 

    print("outgoing date "+ str(theNextDay))

    return theNextDay



def CheckDueDate(mydate,when):

    print(mydate)
    print("the date of the file date is: "+str(datetime.datetime.fromtimestamp(mydate)))
   
    myInputDate = datetime.datetime.fromtimestamp(mydate)

    myOut = None

    if setPassDay(myInputDate) < datetime.datetime.now():
        print("es mas grande")
        print("ya vencio")
        myOut = True
        pass
    else:
        print("es mas chico")
        print("todavia no vencio")
        myOut = False
        pass

    return myOut

#print(CheckDueDate(getLastUpdateOfFile("covid_3.sql"),"1 day at 8 pm"))


# check if db exist

    # check if the expiration date has passed

        # do
            # delete csv
            # delete db
            # download csv
            # create db
        
        # pass

    # do
        # download csv
        # create db
filename="covid_3.sql"



import os,requests
def download(url):
    get_response = requests.get(url,stream=True)
    file_name  = url.split("/")[-1]
    with open(file_name, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

def createDB(csvpath,dbpath):
    #read the CSV
    #df = pd.read_csv('./data/casoscovid19.csv')
    df = pd.read_csv(csvpath)
    #connect to a database
    #conn = sqlite3.connect("casoscovid19.db") 
    conn = sqlite3.connect(dbpath) 
    #if the db does not exist, this creates a Any_Database_Name.db file in the current directory
    #store your table in the database:


    cursor = conn.cursor()
    #Doping EMPLOYEE table if already exists
    cursor.execute("DROP TABLE IF EXISTS mydb")
    #print("Table dropped... ")
    #Commit your changes in the database
    conn.commit()
    #Closing the connection
    #conn.close()
    # https://www.tutorialspoint.com/python_sqlite/python_sqlite_drop_table.htm

    #gg = pd.read_sql('DROP TABLE IF EXISTS test_0;', conn)
    #pd.read_sql_query('DROP TABLE IF EXISTS test_0;', conn)
    df.to_sql('mydb', conn)
    pass

def onlyConnectToDB():
    pass


def downloadAndCreateDB():
    #Downloader
    # https://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
    url = "https://sisa.msal.gov.ar/datos/descargas/covid-19/files/Covid19Casos.csv"

    download(url,pathtosave)
    createDB(pathtosave)
    pass

def deleteAndRemoveDB():
    pass

# test if file exist
# https://linuxize.com/post/python-check-if-file-exists/
import os.path

if os.path.isfile(filepath):
    print ("File exist")

    # test if file pass the due date
    if CheckDueDate(getLastUpdateOfFile(filepath),"1 day at 8 pm"):
        print("pass the due date")
        deleteAndRemoveDB()
        downloadAndCreateDB()
        pass
    else:
        onlyConnectToDB()
        print("not pass the due date")
        print("all okay")
        pass
else:
    print ("File not exist")
    downloadAndCreateDB()





