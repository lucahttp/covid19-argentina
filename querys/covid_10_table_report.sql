SELECT fecha_apertura  AS "Fecha" , residencia_provincia_nombre,
	 count(*) AS "Cantidad de test",
    sum(case when clasificacion_resumen="Confirmado" then 1 else 0 end) AS Confirmados,
    sum(case when clasificacion LIKE "%No Activo%" then 1 else 0 end) AS Recuperados,
    (sum(case when clasificacion_resumen="Confirmado" then 1 else 0 end)-sum(case when clasificacion LIKE "%No Activo%" then 1 else 0 end))Activos,
    sum(case when clasificacion = "Caso confirmado - Fallecido" then 1 else 0 end) AS Fallecidos
FROM mydb
GROUP BY fecha_apertura, residencia_provincia_nombre
ORDER BY "fecha_apertura" DESC,"residencia_provincia_id" ASC,"residencia_departamento_nombre" ASC,"residencia_departamento_nombre" ASC;




SELECT fecha_apertura  AS "Fecha",
	 count(*) AS "Cantidad de test",
    sum(case when clasificacion_resumen="Confirmado" then 1 else 0 end) AS Confirmados,
    sum(case when clasificacion LIKE "%No Activo%" then 1 else 0 end) AS Recuperados,
    (sum(case when clasificacion_resumen="Confirmado" then 1 else 0 end)-sum(case when clasificacion LIKE "%No Activo%" then 1 else 0 end))Activos,
    sum(case when clasificacion = "Caso confirmado - Fallecido" then 1 else 0 end) AS Fallecidos
FROM mydb
GROUP BY fecha_apertura
ORDER BY "fecha_apertura" DESC;

SELECT fecha_apertura, count(*) FROM mydb WHERE (clasificacion_resumen="Confirmado") group by fecha_apertura  ORDER BY "fecha_apertura" DESC;



SELECT fecha_apertura, count(*) FROM mydb WHERE (clasificacion_resumen="Confirmado") group by fecha_apertura  ORDER BY "fecha_apertura" DESC LIMIT 7;

SELECT * FROM mydb
WHERE residencia_departamento_nombre LIKE '%Maipu%'
GROUP BY residencia_departamento_nombre;