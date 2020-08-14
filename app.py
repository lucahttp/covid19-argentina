import os, time, datetime
from datetime import timedelta

import pandas as pd 
import sqlite3

from flask import json
from flask import Flask

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




def downloadCSV():
    #Downloader
    # https://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
    url = "https://sisa.msal.gov.ar/datos/descargas/covid-19/files/Covid19Casos.csv"

    import os
    directory = './data/'
    if not os.path.exists(directory):
        os.makedirs(directory)
        download(url,'./data/casoscovid19.csv')
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



def workWithOnlyCSV():
    try:
        gg = CheckDueDate(getLastUpdateOfFile(filepath),"1 day at 8 pm")
        if gg:
            print("pass the due date")
            deleteAndRemove('./data/casoscovid19.csv')
            downloadCSV()
            pass
        else:
            print("not pass the due date")
            print("all okay")
            print()
            print ("we only create the connection to the DB")
            pass
        pass
    except FileNotFoundError:
        gg = False
        downloadCSV()
        pass






def totalCasosConfirmados():
    workWithOnlyCSV()
    # https://www.geeksforgeeks.org/python-filtering-data-with-pandas-query-method/
    # importing pandas package 
    import pandas as pd 
    
    # making data frame from csv file  
    data = pd.read_csv("./data/casoscovid19.csv") 
    
    # replacing blank spaces with '_'  
    data.columns =[column.replace(" ", "_") for column in data.columns] 
    
    # filtering with query method 
    #print(len(data.query('clasificacion_resumen =="Confirmado"', inplace = True)))
    return len(data.query('clasificacion_resumen =="Confirmado"'))



"""
SELECT residencia_departamento_nombre  AS Residencia,residencia_provincia_nombre  AS Provincia,
    count(*) AS Total,
    sum(case when clasificacion_resumen="Confirmado" then 1 else 0 end) AS Confirmados,
    sum(case when clasificacion LIKE "%No Activo%" then 1 else 0 end) AS Recuperados,
    sum(case when clasificacion = "Caso confirmado - Fallecido" then 1 else 0 end) AS Fallecidos
FROM mydb
GROUP BY residencia_departamento_nombre
ORDER BY "residencia_provincia_id" ASC,"residencia_departamento_nombre" ASC,"residencia_departamento_nombre" ASC;
"""
def moredata():
    workWithOnlyCSV()
    # https://www.geeksforgeeks.org/python-filtering-data-with-pandas-query-method/
    # importing pandas package 
    import pandas as pd 
    
    # making data frame from csv file  
    data = pd.read_csv("./data/casoscovid19.csv") 
    
    # replacing blank spaces with '_'  
    data.columns =[column.replace(" ", "_") for column in data.columns] 
    
    # filtering with query method 
    #print(len(data.query('clasificacion_resumen =="Confirmado"', inplace = True)))
    return len(data.query('clasificacion_resumen =="Confirmado"'))




# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
#y = json.loads(x)

# the result is a Python dictionary:


workWithOnlyCSV()

app = Flask(__name__)

#data = 'hola : luca'

def make_summary():
    x = '{"name":"luca"}'
    x = '{"casos":'+str(totalCasosConfirmados())+'}'
    data = json.loads(x)
    return data

@app.route('/', methods=['GET', 'POST'])
def summary():
    data = make_summary()
    response = app.response_class(
        response=json.dumps(data),
        #response=data,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/test', methods=['GET', 'POST'])
def test():
    data = moredata()
    response = app.response_class(
        response=json.dumps(data),
        #response=data,
        status=200,
        mimetype='application/json'
    )
    return response

# app.run()
# https://stackoverflow.com/questions/41105733/limit-ram-usage-to-python-program
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


# https://blog.miguelgrinberg.com/post/running-a-flask-application-as-a-service-with-systemd

# c:\python27\python.exe -m pip install --upgrade pip
# c:\python38\python.exe -m pip install --upgrade pip
# C:/Python38/python.exe -m pip install thread