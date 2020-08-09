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



mytable='mydb'
#Downloader
# https://medium.com/@petehouston/download-files-with-progress-in-python-96f14f6417a2

import requests
def download(url,filefolder):

    myfile = requests.get(url, allow_redirects=True)

    open(filefolder, 'wb').write(myfile.content)
    pass


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
    df.to_sql(mytable, conn)
    pass

def onlyConnectToDB():
    print ("we only create the connection to the DB")
    #connect to a database
    conn = sqlite3.connect("casoscovid19.db")
    pass


def downloadAndCreateDB():
    #Downloader
    # https://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
    url = "https://sisa.msal.gov.ar/datos/descargas/covid-19/files/Covid19Casos.csv"

    import os
    directory = './data/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    download(url,'./data/casoscovid19.csv')
    createDB('./data/casoscovid19.csv',"./data/casoscovid19.db")
    pass

def deleteAndRemove(filePath):
    import os
    #filePath = '/home/somedir/Documents/python/logs';
    # As file at filePath is deleted now, so we should check if file exists or not not before deleting them
    if os.path.exists(filePath):
        os.remove(filePath)
    else:
        print("Can not delete the file as it doesn't exists")
    pass


filepath = './data/casoscovid19.csv'
# test if file exist
# https://linuxize.com/post/python-check-if-file-exists/
import os.path

if os.path.isfile(filepath):
    print ("File exist")

    # test if file pass the due date
    if CheckDueDate(getLastUpdateOfFile(filepath),"1 day at 8 pm"):
        print("pass the due date")
        deleteAndRemove('./data/casoscovid19.csv')
        deleteAndRemove("./data/casoscovid19.db")
        downloadAndCreateDB()
        pass
    else:
        print("not pass the due date")
        print("all okay")
        print()
        print ("we only create the connection to the DB")
        #connect to a database
        conn = sqlite3.connect("./data/casoscovid19.db")
        pass
else:
    print ("File not exist")
    downloadAndCreateDB()




# table departamentos buenos aires
# Provincia	Casos Confirmados Totales	Recuperados	Fallecidos
sql_string = '''
SELECT fecha_apertura, count(*) FROM '''+mytable+''' WHERE (clasificacion_resumen="Confirmado") group by fecha_apertura  ORDER BY "fecha_apertura" DESC LIMIT 7;
'''
gg = pd.read_sql(sql_string, conn)
print()
print(gg)



# table argentina
# Provincia	Casos Confirmados Totales	Recuperados	Fallecidos
sql_string = '''SELECT count(*) AS Total,
    sum(case when clasificacion_resumen="Confirmado" then 1 else 0 end) AS Confirmados,
    sum(case when clasificacion LIKE "%No Activo%" then 1 else 0 end) AS Recuperados,
    sum(case when clasificacion = "Caso confirmado - Fallecido" then 1 else 0 end) AS Fallecidos
FROM '''+mytable+''';
'''
gg = pd.read_sql(sql_string, conn)
print()
print(gg)

# table provincias
# Provincia	Casos Confirmados Totales	Recuperados	Fallecidos
sql_string = '''SELECT residencia_provincia_nombre  AS Provincia,
    count(*) AS Total,
    sum(case when clasificacion_resumen="Confirmado" then 1 else 0 end) AS Confirmados,
    sum(case when clasificacion LIKE "%No Activo%" then 1 else 0 end) AS Recuperados,
    sum(case when clasificacion = "Caso confirmado - Fallecido" then 1 else 0 end) AS Fallecidos
FROM '''+mytable+'''
GROUP BY residencia_provincia_nombre;
'''
gg = pd.read_sql(sql_string, conn)
print()
print(gg)

# table departamentos buenos aires
# Provincia	Casos Confirmados Totales	Recuperados	Fallecidos
sql_string = '''SELECT residencia_departamento_nombre  AS Residencia,
    count(*) AS Total,
    sum(case when clasificacion_resumen="Confirmado" then 1 else 0 end) AS Confirmados,
    sum(case when clasificacion LIKE "%No Activo%" then 1 else 0 end) AS Recuperados,
    sum(case when clasificacion = "Caso confirmado - Fallecido" then 1 else 0 end) AS Fallecidos
FROM '''+mytable+'''
WHERE (residencia_provincia_nombre="Buenos Aires")
GROUP BY residencia_departamento_nombre;
'''
gg = pd.read_sql(sql_string, conn)
print()
print(gg)





# table departamentos caba
# Caba	Casos Confirmados Totales	Recuperados	Fallecidos


"""
SELECT count(*) FROM '''+mytable+''' WHERE (residencia_provincia_nombre="CABA" AND residencia_departamento_nombre<>"SIN ESPECIFICAR");
SELECT fecha_apertura, count(*) FROM '''+mytable+''' WHERE (clasificacion_resumen="Confirmado") group by fecha_apertura  ORDER BY "fecha_apertura" DESC LIMIT 7;

SELECT * FROM '''+mytable+''' WHERE (residencia_provincia_nombre="CABA");

SELECT * FROM '''+mytable+''' WHERE (residencia_provincia_nombre="CABA" AND residencia_departamento_nombre<>"SIN ESPECIFICAR");
"""
sql_string = '''SELECT residencia_departamento_nombre  AS Residencia,
    count(*) AS Total,
    sum(case when clasificacion_resumen="Confirmado" then 1 else 0 end) AS Confirmados,
    sum(case when clasificacion LIKE "%No Activo%" then 1 else 0 end) AS Recuperados,
    sum(case when clasificacion = "Caso confirmado - Fallecido" then 1 else 0 end) AS Fallecidos
FROM '''+mytable+'''
WHERE (residencia_provincia_nombre="CABA" AND residencia_departamento_nombre<>"SIN ESPECIFICAR")
GROUP BY residencia_departamento_nombre;
'''
gg = pd.read_sql(sql_string, conn)
print()
print(gg)


