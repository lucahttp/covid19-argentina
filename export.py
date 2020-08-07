# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# #Work as SQL
# import pandas as pd
# import sqlite3

# %%
import pandas as pd 
import sqlite3


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
#read a SQL Query out of your database and into a pandas dataframe
sql_string = 'SELECT * FROM test_0'
sql_string = 'SELECT COUNT(*) FROM test_0 WHERE clasificacion LIKE "%Caso confirmado%";'
gg = pd.read_sql(sql_string, conn)
gg


# %%
#read a SQL Query out of your database and into a pandas dataframe
sql_string = 'SELECT * FROM test_0 LIMIT 5;'
gg = pd.read_sql(sql_string, conn)
gg


# %%
# ultima_actualizacion


# %%
sql_string = 'SELECT DISTINCT residencia_departamento_nombre FROM test_0 WHERE residencia_provincia_nombre="Buenos Aires";'
gg = pd.read_sql(sql_string, conn)
gg


# %%
sql_string = 'SELECT DISTINCT residencia_departamento_nombre FROM test_0 WHERE residencia_provincia_nombre="Buenos Aires";'
sql_string = 'select residencia_departamento_nombre, count(*) from test_0 WHERE residencia_provincia_nombre="Buenos Aires" AND clasificacion_resumen="Confirmado" group by residencia_departamento_nombre;'
gg = pd.read_sql(sql_string, conn)
gg



# %%
sql_string = 'SELECT DISTINCT residencia_departamento_nombre FROM test_0 WHERE residencia_provincia_nombre="Buenos Aires";'
gg = pd.read_sql(sql_string, conn)
gg


# %%
sql_string = 'select residencia_departamento_nombre, count(*) from test_0 WHERE residencia_provincia_nombre="Buenos Aires" group by residencia_departamento_nombre;'
gg = pd.read_sql(sql_string, conn)
gg


# %%
sql_string = 'SELECT residencia_departamento_nombre, count(*) FROM test_0 WHERE (residencia_provincia_nombre="Buenos Aires"  AND clasificacion_resumen="Confirmado") group by residencia_departamento_nombre;'
gg = pd.read_sql(sql_string, conn)
gg


# %%
# casos por provincia
sql_string = 'SELECT residencia_provincia_nombre, count(*) FROM test_0 WHERE (clasificacion_resumen="Confirmado") group by residencia_provincia_nombre;'
#sql_string = 'SELECT carga_provincia_nombre, count(*) FROM test_0 WHERE (clasificacion_resumen="Confirmado") group by carga_provincia_nombre;'
gg = pd.read_sql(sql_string, conn)
gg


# %%
sql_string = 'SELECT count(*) FROM test_0 WHERE (clasificacion_resumen="Confirmado");'
gg = pd.read_sql(sql_string, conn)
gg


# %%
sql_string = 'SELECT DISTINCT residencia_departamento_nombre FROM test_0 WHERE residencia_provincia_nombre="Buenos Aires";'
sql_string = 'select residencia_departamento_nombre, count(*) from test_0 WHERE (clasificacion_resumen="Confirmado" AND residencia_provincia_nombre="Buenos Aires") group by residencia_departamento_nombre;'
gg = pd.read_sql(sql_string, conn)
gg


# %%
# muertes por departamento
sql_string = 'select residencia_departamento_nombre, count(*) from test_0 WHERE (clasificacion="Caso confirmado - Fallecido" AND residencia_provincia_nombre="Buenos Aires") group by residencia_departamento_nombre;'
gg = pd.read_sql(sql_string, conn)
gg


# %%
# muertes por provincia
sql_string = 'select residencia_provincia_nombre, count(*) from test_0 WHERE (clasificacion="Caso confirmado - Fallecido") group by residencia_provincia_nombre;'
gg = pd.read_sql(sql_string, conn)
gg


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
print(len(data.query('clasificacion_resumen =="Confirmado"')))
# display 
#data 


# %%
pip install -U pandasql


# %%
# https://stackoverflow.com/questions/30530663/how-to-select-distinct-across-multiple-data-frame-columns-in-pandas
# https://riptutorial.com/pandas/example/26077/select-distinct-rows-across-dataframe
# data = pd.read_csv("./data/casoscovid19.csv") 

# from pandasql import sqldf
# q="""SELECT DISTINCT col1, col2 FROM df;"""
# pysqldf = lambda q: sqldf(q, globals())
# data = pysqldf(q)


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



