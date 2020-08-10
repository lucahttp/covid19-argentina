SELECT residencia_departamento_nombre  AS Residencia,residencia_provincia_nombre  AS Residencia,
    count(*) AS Total,
    sum(case when clasificacion_resumen="Confirmado" then 1 else 0 end) AS Confirmados,
    sum(case when clasificacion LIKE "%No Activo%" then 1 else 0 end) AS Recuperados,
    sum(case when clasificacion = "Caso confirmado - Fallecido" then 1 else 0 end) AS Fallecidos
FROM mydb
GROUP BY residencia_departamento_nombre
ORDER BY "residencia_provincia_id" ASC,"residencia_departamento_nombre" ASC,"residencia_departamento_nombre" ASC;