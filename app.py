from flask import Flask, request, send_from_directory
from multiprocessing import Process
import time
import requests
import os.path
import os
import time
import datetime
from datetime import timedelta

import pandas as pd
import sqlite3

from flask import Flask, request, render_template, json
import os
import time
import datetime
from datetime import timedelta

import pandas as pd
import sqlite3

from flask import Flask
import requests
import time
from multiprocessing import Process
import datetime
from flask import g


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


import pandas as pd


class CovidData:
    def __init__(self, url):
        self.url = url
        self.state = None
        self.LastUpdate = None

        # Files
        #self.filename = "covid_3.sql"
        self.csvfilepath = './data/casoscovid19.csv'
        self.dbfilepath = './data/casoscovid19.db'
        self.mytable = 'mydb'

        self.csvfilereport = "report.csv"

        self.directory = './data/'
        # SQLite
        self.conn = None

        # Data

        self.countAllCases = None

    def getCountAllCases(self):
        return self.countAllCases

    def getStatus(self):
        return self.state

    def setStatus(self, newStatus):
        self.state = newStatus
        print("new status setted")

        # get file date

    def getLastUpdateOfFile(self, file):

        print()
        print("file : "+file)

        created = os.path.getctime(file)
        return created

    # add time to a specific date to create the due date

    def setPassDay(self, mydate):

        #print("incoming date " + str(mydate))

        theNextDay = mydate + timedelta(days=1)
        theNextDay = theNextDay.replace(
            hour=20, minute=00, second=00, microsecond=00)

        #print("outgoing date " + str(theNextDay))

        from tabulate import tabulate
        #print(tabulate([['2020-08-14 16:36:08','2020-08-15 20:00:00','2020-08-14 19:15:00'], []], headers=["File Date", "File Expiration Date","Current Date"]))
        print()
        print(tabulate([[str(mydate.replace(microsecond=00)), str(theNextDay), str(datetime.datetime.now(
        ).replace(microsecond=00))], []], headers=["File Date", "File Expiration Date", "Current Date"]))

        return theNextDay

    def CheckDueDate(self, mydate, when):

        # print(mydate)
        #print("the date of the file date is: " + str(datetime.datetime.fromtimestamp(mydate)))

        from tabulate import tabulate
        print(tabulate([['2020-08-14 16:36:08','2020-08-15 20:00:00','2020-08-14 19:15:00'], []], headers=["File Date", "File Expiration Date","Current Date"]))

        myInputDate = datetime.datetime.fromtimestamp(mydate)

        myOut = None

        if self.setPassDay(myInputDate) < datetime.datetime.now():
            #print("es mas grande")
            #print("ya vencio"+" - es mas grande")
            myOut = True
            pass
        else:
            #print("es mas chico")
            #print("vencido = "+str(covidargentina.CheckData()))
            #print("todavia no vencio"+" - es mas chico")
            myOut = False
            pass

        print("vencido = "+str(myOut))

        return myOut

    # Downloader
    # https://medium.com/@petehouston/download-files-with-progress-in-python-96f14f6417a2

    # import requests
    def download(self, url, filefolder):
        print("Download started")
        myfile = requests.get(url, allow_redirects=True)

        open(filefolder, 'wb').write(myfile.content)
        print("Download finished")
        pass

    def downloadCSV(self):
        # Downloader
        # https://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
        print("Downloader")
        import os
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
            self.download(self.url, self.csvfilepath)
            pass
        else:
            self.download(self.url, self.csvfilepath)
            pass

    def deleteAndRemove(self, filetopath):
        import os
        #filePath = '/home/somedir/Documents/python/logs';
        # As file at filePath is deleted now, so we should check if file exists or not not before deleting them
        try:
            os.remove(filetopath)
            pass
        except FileNotFoundError:
            print("Can not delete the file as it doesn't exists")
            pass
        """
        if os.path.exists(filetopath):
            os.remove(filetopath)
        else:
            print("Can not delete the file as it doesn't exists")
        pass
        """

    def createDB(self, csvpath, dbpath):
        # read the CSV
        #df = pd.read_csv('./data/casoscovid19.csv')
        df = pd.read_csv(csvpath)
        # connect to a database
        #conn = sqlite3.connect("casoscovid19.db")
        self.conn = sqlite3.connect(dbpath)
        # if the db does not exist, this creates a Any_Database_Name.db file in the current directory
        # store your table in the database:

        cursor = self.conn.cursor()
        # Doping EMPLOYEE table if already exists
        cursor.execute("DROP TABLE IF EXISTS mydb;")
        #print("Table dropped... ")
        # Commit your changes in the database
        self.conn.commit()
        # Closing the connection
        # conn.close()
        # https://www.tutorialspoint.com/python_sqlite/python_sqlite_drop_table.htm

        #gg = pd.read_sql('DROP TABLE IF EXISTS test_0;', conn)
        #pd.read_sql_query('DROP TABLE IF EXISTS test_0;', conn)
        df.to_sql("mydb", self.conn)
        pass

    def onlyConnectToDB(self):
        print("we only create the connection to the DB")
        # connect to a database
        self.conn = sqlite3.connect(self.dbfilepath)
        pass

    def CheckData(self):
        try:        
            result = self.CheckDueDate(self.getLastUpdateOfFile(self.csvfilepath), "1 day at 8 pm")
            return result
        except FileNotFoundError:
            print("No funciona")
            self.deleteAndRemove(self.csvfilepath)
            self.deleteAndRemove(self.dbfilepath)
            self.downloadCSV()
            self.createDB(self.csvfilepath, self.dbfilepath)
            """
            self.createDB(self.csvfilepath, self.dbfilepath)
            self.conn = sqlite3.connect(self.dbfilepath)
            
            """
            pass


    def checkAllsGood(self):
        if os.path.isfile(self.csvfilepath):
            print("File exist")

            # test if file pass the due date
            if self.CheckDueDate(self.getLastUpdateOfFile(self.csvfilepath), "1 day at 8 pm"):
                print("pass the due date")
                self.deleteAndRemove(self.csvfilepath)
                self.deleteAndRemove(self.dbfilepath)
                self.downloadCSV()
                self.createDB(self.csvfilepath, self.dbfilepath)
                self.conn = sqlite3.connect(self.dbfilepath)
                pass
            else:
                print("not pass the due date")
                print("all okay")
                print()
                print("we only create the connection to the DB")
                # connect to a database
                self.createDB(self.csvfilepath, self.dbfilepath)
                self.conn = sqlite3.connect(self.dbfilepath)
                pass
        else:
            print("File not exist")
            self.downloadCSV()
            self.createDB(self.csvfilepath, self.dbfilepath)
            self.conn = sqlite3.connect(self.dbfilepath)
            pass
        pass
    def superRefresh(self):
        self.deleteAndRemove(self.csvfilepath)
        self.deleteAndRemove(self.dbfilepath)
        self.downloadCSV()
        self.createDB(self.csvfilepath, self.dbfilepath)
        self.conn = sqlite3.connect(self.dbfilepath)
        pass
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

    # test if file exist
    # https://linuxize.com/post/python-check-if-file-exists/

    def workWithOnlyCSV(self):
        try:
            gg = self.CheckDueDate(self.getLastUpdateOfFile(
                self.csvfilepath), "1 day at 8 pm")
            if gg:
                print("pass the due date")
                self.deleteAndRemove(self.csvfilepath)
                self.downloadCSV()
                pass
            else:
                #print("not pass the due date")
                # print("okay")
                # print()
                #print("we only create the connection to the DB")
                pass
            pass
        except FileNotFoundError:
            gg = False
            self.downloadCSV()
            pass

    def totalCasosConfirmados(self):
        self.workWithOnlyCSV()
        # https://www.geeksforgeeks.org/python-filtering-data-with-pandas-query-method/
        # importing pandas package
        # import pandas as pd

        # making data frame from csv file
        data = pd.read_csv("./data/casoscovid19.csv")

        # replacing blank spaces with '_'
        data.columns = [column.replace(" ", "_") for column in data.columns]

        # filtering with query method
        #print(len(data.query('clasificacion_resumen =="Confirmado"', inplace = True)))
        return len(data.query('clasificacion_resumen =="Confirmado"'))

    """
    SELECT residencia_departamento_nombre  AS Residencia,residencia_provincia_nombre  AS Provincia,
        count(*) AS Total,
        sum(case when clasificacion_resumen="Confirmado" then 1 else 0 end) AS Confirmados,
        sum(case when clasificacion LIKE "%No Activo%" then 1 else 0 end) AS Recuperados,
        sum(case when clasificacion = "Caso confirmado - Fallecido" then 1 else 0 end) AS Fallecidos
    FROM self.mytable
    GROUP BY residencia_departamento_nombre
    ORDER BY "residencia_provincia_id" ASC,"residencia_departamento_nombre" ASC,"residencia_departamento_nombre" ASC;
    """

    def moredata(self):
        self.workWithOnlyCSV()
        # https://www.geeksforgeeks.org/python-filtering-data-with-pandas-query-method/
        # importing pandas package
        # import pandas as pd

        # making data frame from csv file
        data = pd.read_csv("./data/casoscovid19.csv")

        # replacing blank spaces with '_'
        data.columns = [column.replace(" ", "_") for column in data.columns]

        # filtering with query method
        #print(len(data.query('clasificacion_resumen =="Confirmado"', inplace = True)))
        self.countAllCases = len(data.query(
            'clasificacion_resumen =="Confirmado"'))
        pass

    def fullreportSimple(self):
        self.checkAllsGood()
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
        gg = pd.read_sql(sql_string, self.conn)
        print()

        import json
        # print(type(gg))
        #gg = gg.set_index(0)
        print(type(gg))
        gg.to_csv("report.csv", encoding='latin1', index=False)
        #json.dumps(parsed, indent=4, ensure_ascii=False)
        # gg.set_index(list(gg)[0])
        gg = gg.set_index(gg.columns[0])
        gg.set_index(gg.columns.tolist()[0])
        #json.dumps(parsed, indent=4)

        result = gg.to_json(orient="index")
        parsed = json.loads(result)
        resultado = gg.to_json(orient="index")
        gg.to_json("report.json", orient='table', force_ascii=False, indent=4)

        # Works
        #out = json.dumps(parsed, indent=4, ensure_ascii=False)
        #gg.to_csv('report.csv', encoding='utf-8', index=False)

        #result = gg.to_json(orient="index")

        parsed = json.loads(result)

        json.dumps(parsed, indent=4)
        # print(resultado)
        return resultado

    def fullreport(self):
        covidargentina.checkAllsGood()
        # https://stackoverflow.com/questions/4899832/sqlite-function-to-format-numbers-with-leading-zeroes
        # https://tiebing.blogspot.com/2011/07/sqlite-3-string-to-integer-conversion.html
        """
        CAST(substr('00'||residencia_provincia_id,-2) || substr('000'||residencia_departamento_id,-3) as integer) AS ID,
        """
        sql_string = """
        SELECT residencia_departamento_nombre  AS "Departamento Residencia",residencia_provincia_nombre  AS "Provincia Residencia", 
        substr('00'||residencia_provincia_id,-2) || substr('000'||residencia_departamento_id,-3) AS ID,
        substr('000'||residencia_departamento_id,-3) AS "ID Departamento",
        substr('00'||residencia_provincia_id,-2) AS "ID Provincia",
        count(*) AS "Total Test",
        sum(case when clasificacion_resumen="Confirmado" then 1 else 0 end) AS Confirmados,
        sum(case when clasificacion LIKE "%No Activo%" then 1 else 0 end) AS Recuperados,
        (sum(case when clasificacion_resumen="Confirmado" then 1 else 0 end)-sum(case when clasificacion LIKE "%No Activo%" then 1 else 0 end))Activos,
        sum(case when clasificacion = "Caso confirmado - Fallecido" then 1 else 0 end) AS Fallecidos
        FROM mydb
        GROUP BY residencia_departamento_nombre
        ORDER BY "residencia_provincia_id" ASC,"residencia_departamento_nombre" ASC,"residencia_departamento_nombre" ASC;
        """
        gg = pd.read_sql(sql_string, self.conn)
        print()

        import json
        # print(type(gg))
        #gg = gg.set_index(0)
        print(type(gg))
        gg.to_csv("report.csv", encoding='latin1', index=False)
        #json.dumps(parsed, indent=4, ensure_ascii=False)
        # gg.set_index(list(gg)[0])
        gg = gg.set_index(gg.columns[0])
        gg.set_index(gg.columns.tolist()[0])
        #json.dumps(parsed, indent=4)

        result = gg.to_json(orient="index")
        parsed = json.loads(result)
        resultado = gg.to_json(orient="index")
        gg.to_json("report.json", orient='table', force_ascii=False, indent=4)

        # Works
        #out = json.dumps(parsed, indent=4, ensure_ascii=False)
        #gg.to_csv('report.csv', encoding='utf-8', index=False)

        #result = gg.to_json(orient="index")

        parsed = json.loads(result)

        json.dumps(parsed, indent=4)
        # print(resultado)
        return resultado

    def reportcsv(self):
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
        gg = pd.read_sql(sql_string, self.conn)
        print()

        import json
        # print(type(gg))
        #gg = gg.set_index(0)
        print(type(gg))

        return gg.to_csv(encoding='latin1', index=False)


# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'


url = "https://sisa.msal.gov.ar/datos/descargas/covid-19/files/Covid19Casos.csv"
covidargentina = CovidData(url)
#covidargentina.getStatus()

#print("vencido = "+str(covidargentina.CheckData()))
#covidargentina.downloadCSV()
# Define some heavy function
#covidargentina.checkAllsGood()
#covidargentina.setStatus("Process started")

# print(covidargentina.getStatus())
# time.sleep(10)


#covidargentina.setStatus("Process finished")

# print(covidargentina.getStatus())


#print("vencido = "+str(covidargentina.CheckData()))

# print()
# print(covidargentina.moredata())

# parse x:
#y = json.loads(x)

# the result is a Python dictionary:


# covidargentina.checkAllsGood()
print("GG")
# covidargentina.createDB(covidargentina.csvfilepath,covidargentina.dbfilepath)
# datosqwe = covidargentina.fullreport()
# print(datosqwe)


def make_summary_csv():
    return covidargentina.reportcsv()

# workWithOnlyCSV()


def myfunct():
    print("gg")
    covidargentina.moredata()
    pass


app = Flask(__name__, static_folder='static', static_url_path='')

# Async in flask
# https://stackoverflow.com/questions/31866796/making-an-asynchronous-task-in-flask


@app.route('/render/<id>', methods=['GET'])
def render_script(id=None):
    ...
    heavy_process = Process(  # Create a daemonic process with heavy "my_func"
        target=myfunct(),
        daemon=True
    )
    heavy_process.start()

    # return Response(mimetype='application/json', status=200)
    data = covidargentina.getCountAllCases()
    response = app.response_class(
        response="GG",
        # response=data,
        status=200,
        mimetype='text/plain'
    )
    return response

#data = 'hola : luca'


@app.route('/render/', methods=['POST', 'GET'])
def script():
    ...
    heavy_process = Process(  # Create a daemonic process with heavy "my_func"
        target=my_func,
        daemon=True
    )
    heavy_process.start()

    dataso = open('report.json')
    response = app.response_class(
        response=dataso.read(),
        # response=data,
        status=200,
        mimetype='application/json'
        # text/plain, text/html, text/css, text/javascript application/json
        # https://developer.mozilla.org/es/docs/Web/HTTP/Basics_of_HTTP/MIME_types
    )
    return response

# Define some heavy function


def my_func():
    # time.sleep(1)
    print("Download process started")
    covidargentina.checkAllsGood()
    print("Download process finished")

    print("Build DB process started")
    covidargentina.fullreport()
    print("Build DB  process finished")
    # setData()
    pass


def make_summary():
    x = '{"name":"luca"}'
    x = '{"casos":'+str(covidargentina.totalCasosConfirmados())+'}'
    data = json.loads(x)
    return data


@app.route('/preview', methods=['GET', 'POST'])
def preview():
    return render_template('table.html')


"""
@app.route('/', methods=['GET', 'POST'])
def summary():
    data = make_summary()
    response = app.response_class(
        response=json.dumps(data),
        # response=data,
        status=200,
        mimetype='application/json'
    )
    return response
"""


"""
def make_summary2():
    covidargentina.checkAllsGood()
    dato = covidargentina.fullreport()
    # x = '{"casos":'+str(covidargentina.totalCasosConfirmados())+'}'
    data = json.loads(dato)
    return data



@app.route('/report', methods=['GET', 'POST'])
def summary2():
    data = make_summary2()
    
    response = app.response_class(
        response=json.dumps(data),
        # response=data,
        status=200,
        mimetype='application/json'
    )
    return response

"""
# app.py
"""
@app.route('/preview/csv')
def get_d3_data():
    filename = covidargentina.csvfilereport
    #data = pd.read_csv(filename, header=0, encoding='latin1')
    #df = pd.read_csv(filename, header=0, encoding='latin1')
    df = pd.read_csv(filename, encoding='latin1')
    print(df)
    return str(df)
@app.route('/preview/csv', methods=['GET', 'POST'])
def home():
    return send_from_directory('/', covidargentina.csvfilereport)
"""
"""
@app.route('/preview/gg/json', methods=['GET', 'POST'])
def asd():
    f = open('report.json')
    response = app.response_class(
        response=f.read(),
        # response=data,
        status=200,
        mimetype='application/json'
        # text/plain, text/html, text/css, text/javascript application/json 
        # https://developer.mozilla.org/es/docs/Web/HTTP/Basics_of_HTTP/MIME_types
    )
    return response
def my_refresh():
    # time.sleep(1)
    print("Refresh process started")
    covidargentina.superRefresh()
    #covidargentina.deleteAndRemove(covidargentina.csvfilepath)
    #covidargentina.deleteAndRemove(covidargentina.dbfilepath)
    #print("Download process started")
    #covidargentina.downloadCSV()
    #print("Download process finished")
    #covidargentina.checkAllsGood()

    #print("Build DB process started")
    #covidargentina.fullreport()
    #print("Build DB  process finished")
    print("Refresh process finished")
    # setData()
    pass



@app.route('/preview/csv', methods=['GET', 'POST'])
def catch_all():
    f = open('report.csv')
    return f.read()


@app.route('/', methods=['GET', 'POST'])
def test():
    covidargentina.moredata()
    data = covidargentina.getCountAllCases()
    response = app.response_class(
        response=json.dumps(data),
        # response=data,
        status=200,
        mimetype='text/plain'
        # text/plain, text/html, text/css, text/javascript application/json
        # https://developer.mozilla.org/es/docs/Web/HTTP/Basics_of_HTTP/MIME_types
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
