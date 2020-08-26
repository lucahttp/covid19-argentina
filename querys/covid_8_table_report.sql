SELECT residencia_departamento_nombre  AS "Departamento Residencia",residencia_provincia_nombre  AS "Provincia Residencia", residencia_departamento_id AS "ID Departamento", residencia_provincia_id AS "ID Provincia",
    count(*) AS "Total Test",
    sum(case when clasificacion_resumen="Confirmado" then 1 else 0 end) AS Confirmados,
    sum(case when clasificacion LIKE "%No Activo%" then 1 else 0 end) AS Recuperados,
    (sum(case when clasificacion_resumen="Confirmado" then 1 else 0 end)-sum(case when clasificacion LIKE "%No Activo%" then 1 else 0 end))Activos,
    sum(case when clasificacion = "Caso confirmado - Fallecido" then 1 else 0 end) AS Fallecidos
FROM mydb
GROUP BY residencia_departamento_nombre
ORDER BY "residencia_provincia_id" ASC,"residencia_departamento_nombre" ASC,"residencia_departamento_nombre" ASC;