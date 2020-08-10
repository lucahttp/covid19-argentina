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

def checkAllsGood():
if os.path.isfile(filepath):
    print ("File exist")

    # test if file pass the due date
    if CheckDueDate(getLastUpdateOfFile(filepath),"1 day at 8 pm"):
        print("pass the due date")
        deleteAndRemove('./data/casoscovid19.csv')
        deleteAndRemove("./data/casoscovid19.db")
        downloadAndCreateDB()
        
        conn = sqlite3.connect("./data/casoscovid19.db")
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
    conn = sqlite3.connect("./data/casoscovid19.db")



def datosdepartamentosbuenosaires():
    # table departamentos buenos aires
    # Provincia	Casos Confirmados Totales	Recuperados	Fallecidos
    sql_string = '''
    SELECT fecha_apertura, count(*) FROM '''+mytable+''' WHERE (clasificacion_resumen="Confirmado") group by fecha_apertura  ORDER BY "fecha_apertura" DESC LIMIT 7;
    '''
    gg = pd.read_sql(sql_string, conn)
    print()
    print(gg)
    pass


def datostableargentina():
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
    pass

def datostableprovincias():
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
    pass


def datostabledepartamentosbuenosaires():
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
    pass





def datostabledepartamentoscaba():
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
    pass


def totalCasosConfirmados():
    # %%
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
    # display 
    #data 
    pass

def fullreport():
    sql_string = """
    SELECT residencia_departamento_nombre  AS Residencia,residencia_provincia_nombre  AS Provincia,
        count(*) AS Total,
        sum(case when clasificacion_resumen="Confirmado" then 1 else 0 end) AS Confirmados,
        sum(case when clasificacion LIKE "%No Activo%" then 1 else 0 end) AS Recuperados,
        sum(case when clasificacion = "Caso confirmado - Fallecido" then 1 else 0 end) AS Fallecidos
    FROM mydb
    GROUP BY residencia_departamento_nombre
    ORDER BY "residencia_provincia_id" ASC,"residencia_departamento_nombre" ASC,"residencia_departamento_nombre" ASC;
    """
    gg = pd.read_sql(sql_string, conn)
    print()

    import json
    #print(type(gg))
    #gg = gg.set_index(0)
    print(type(gg))
    gg.to_csv("report.csv", encoding='latin1', index=False)
    #json.dumps(parsed, indent=4, ensure_ascii=False)
    ##gg.set_index(list(gg)[0])
    gg = gg.set_index(gg.columns[0])
    gg.set_index(gg.columns.tolist()[0])
    #json.dumps(parsed, indent=4)  

    result = gg.to_json(orient="index")
    parsed = json.loads(result)
    resultado = gg.to_json(orient="index")
    gg.to_json("report.json", orient ='table',force_ascii=False) 

    #Works
    #out = json.dumps(parsed, indent=4, ensure_ascii=False)
    #gg.to_csv('report.csv', encoding='utf-8', index=False)


    #result = gg.to_json(orient="index")

    parsed = json.loads(result)

    json.dumps(parsed, indent=4)  
    #print(resultado)
    return resultado


from flask import json
from flask import Flask

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:


app = Flask(__name__)

#data = 'hola : luca'
mydata = fullreport()

def make_summary():
    data = 'hola : luca'
    data = y
    return data

# Memory Usage

import sys
import resource

def memory_limit():
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (get_memory() * 1024 / 2, hard))

def get_memory():
    with open('/proc/meminfo', 'r') as mem:
        free_memory = 0
        for i in mem:
            sline = i.split()
            if str(sline[0]) in ('MemFree:', 'Buffers:', 'Cached:'):
                free_memory += int(sline[1])
    return free_memory



# c:\python27\python.exe -m pip install --upgrade pip
# c:\python38\python.exe -m pip install --upgrade pip


# https://flask-limiter.readthedocs.io/en/stable/
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)



app.testing = True

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)
@app.route("/slow")
@limiter.limit("1 per day")
def slow():
    return ":("

@app.route("/medium")
@limiter.limit("1/second", override_defaults=False)
def medium():
    return ":|"

@app.route("/fast")
def fast():
    return ":)"

@app.route("/ping")
@limiter.exempt
def ping():
    return "PONG"

    
@app.route("/hola")
@limiter.exempt
def hola():
    return "HOLA2"


@app.route('/')
@limiter.limit("1/second", override_defaults=False)
def summary():
    data = mydata
    response = app.response_class(
        response=data,
        #response=data,
        status=200,
        mimetype='application/json'
    )
    return response
@app.route('/json', methods=['GET', 'POST'])
@limiter.limit("1/second", override_defaults=False)
def add_message():
    with open('report.json', 'r') as myfile:
        data=myfile.read()
    # parse file
    obj = json.loads(data)
    return obj


# app.run()
# https://stackoverflow.com/questions/41105733/limit-ram-usage-to-python-program
if __name__ == '__main__':
    memory_limit() # Limitates maximun memory usage to half
    try:
        #main()
        app.run(debug=True, use_reloader=True)
    except MemoryError:
        sys.stderr.write('\n\nERROR: Memory Exception\n')
        sys.exit(1)


# https://blog.miguelgrinberg.com/post/running-a-flask-application-as-a-service-with-systemd