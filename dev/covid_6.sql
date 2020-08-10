


SELECT DISTINCT "residencia_departamento_nombre",residencia_provincia_nombre FROM "mydb" ORDER BY "residencia_provincia_id" ASC,"residencia_departamento_nombre" ASC,"residencia_departamento_nombre" ASC;



SELECT "residencia_departamento_nombre"  AS Residencia,residencia_provincia_nombre,
    count(*) AS Total,
    sum(case when clasificacion_resumen="Confirmado" then 1 else 0 end) AS Confirmados,
    sum(case when clasificacion LIKE "%No Activo%" then 1 else 0 end) AS Recuperados,
    sum(case when clasificacion = "Caso confirmado - Fallecido" then 1 else 0 end) AS Fallecidos
FROM mydb

ORDER BY "residencia_provincia_id" ASC,"residencia_departamento_nombre" ASC,"residencia_departamento_nombre" ASC;



SELECT DISTINCT "residencia_departamento_nombre",residencia_provincia_nombre FROM "mydb" ORDER BY "residencia_provincia_id" ASC,"residencia_departamento_nombre" ASC,"residencia_departamento_nombre" ASC;



SELECT DISTINCT "residencia_departamento_nombre",residencia_provincia_nombre FROM "mydb" ORDER BY "residencia_provincia_id" ASC,"residencia_departamento_nombre" ASC,"residencia_departamento_nombre" ASC;



SELECT DISTINCT "residencia_departamento_nombre",residencia_provincia_nombre FROM "mydb" WHERE (residencia_provincia_nombre="CABA" );

SELECT residencia_departamento_nombre FROM mydb GROUP BY residencia_provincia_nombre;



SELECT residencia_departamento_nombre AS Departamento,residencia_provincia_nombre AS provincia FROM mydb GROUP BY residencia_provincia_nombre;



SELECT residencia_departamento_nombre  AS Residencia FROM mydb;

SELECT DISTINCT residencia_departamento_nombre FROM mydb; 

