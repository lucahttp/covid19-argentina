# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# #Work as SQL

# %%
import pandas as pd 
import sqlite3


# %%
#Downloader
# https://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
url = "https://sisa.msal.gov.ar/datos/descargas/covid-19/files/Covid19Casos.csv"


import os,requests
def download(url):
    get_response = requests.get(url,stream=True)
    file_name  = url.split("/")[-1]
    with open(file_name, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
download(url)



# %%
pip3 install wget


# %%
#Downloader
# https://medium.com/@petehouston/download-files-with-progress-in-python-96f14f6417a2
url = "https://sisa.msal.gov.ar/datos/descargas/covid-19/files/Covid19Casos.csv"

import wget
def download(url):
    def bar_custom(current, total, width=80):
        print("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))
    wget.download(url,'./test/',bar=bar_custom)

download(url)


# %%
#read the CSV
df = pd.read_csv('./data/casoscovid19.csv')
#connect to a database
conn = sqlite3.connect("casoscovid19.db") #if the db does not exist, this creates a Any_Database_Name.db file in the current directory
#store your table in the database:


cursor = conn.cursor()
#Doping EMPLOYEE table if already exists
cursor.execute("DROP TABLE IF EXISTS test_0")
#print("Table dropped... ")
#Commit your changes in the database
conn.commit()
#Closing the connection
#conn.close()
# https://www.tutorialspoint.com/python_sqlite/python_sqlite_drop_table.htm

#gg = pd.read_sql('DROP TABLE IF EXISTS test_0;', conn)
#pd.read_sql_query('DROP TABLE IF EXISTS test_0;', conn)
df.to_sql('test_0', conn)


# %%
#connect to a database
conn = sqlite3.connect("casoscovid19.db") 
#if the db does not exist, this creates a Any_Database_Name.db file in the current directory


# %%
# table argentina
# Provincia	Casos Confirmados Totales	Recuperados	Fallecidos
sql_string = '''SELECT count(*) AS Total,
    sum(case when clasificacion_resumen="Confirmado" then 1 else 0 end) AS Confirmados,
    sum(case when clasificacion LIKE "%No Activo%" then 1 else 0 end) AS Recuperados,
    sum(case when clasificacion = "Caso confirmado - Fallecido" then 1 else 0 end) AS Fallecidos
FROM test_0;
'''
gg = pd.read_sql(sql_string, conn)
gg


# %%
# table provincias
# Provincia	Casos Confirmados Totales	Recuperados	Fallecidos
sql_string = '''SELECT residencia_provincia_nombre  AS Provincia,
    count(*) AS Total,
    sum(case when clasificacion_resumen="Confirmado" then 1 else 0 end) AS Confirmados,
    sum(case when clasificacion LIKE "%No Activo%" then 1 else 0 end) AS Recuperados,
    sum(case when clasificacion = "Caso confirmado - Fallecido" then 1 else 0 end) AS Fallecidos
FROM test_0
GROUP BY residencia_provincia_nombre;
'''
gg = pd.read_sql(sql_string, conn)
gg


# %%
# table departamentos buenos aires
# Provincia	Casos Confirmados Totales	Recuperados	Fallecidos
sql_string = '''SELECT residencia_departamento_nombre  AS Residencia,
    count(*) AS Total,
    sum(case when clasificacion_resumen="Confirmado" then 1 else 0 end) AS Confirmados,
    sum(case when clasificacion LIKE "%No Activo%" then 1 else 0 end) AS Recuperados,
    sum(case when clasificacion = "Caso confirmado - Fallecido" then 1 else 0 end) AS Fallecidos
FROM test_0
WHERE (residencia_provincia_nombre="Buenos Aires")
GROUP BY residencia_departamento_nombre;
'''
gg = pd.read_sql(sql_string, conn)
gg


# %%
# table departamentos buenos aires
# Provincia	Casos Confirmados Totales	Recuperados	Fallecidos
sql_string = '''
SELECT fecha_apertura, count(*) FROM test_0 WHERE (clasificacion_resumen="Confirmado") group by fecha_apertura  ORDER BY "fecha_apertura" DESC LIMIT 7;
'''
gg = pd.read_sql(sql_string, conn)
gg


# %%



