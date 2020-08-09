
SELECT residencia_departamento_nombre  AS Residencia,
    count(*) AS Total,
    sum(case when clasificacion_resumen="Confirmado" then 1 else 0 end) AS Confirmados,
    sum(case when clasificacion LIKE "%No Activo%" then 1 else 0 end) AS Recuperados,
    sum(case when clasificacion = "Caso confirmado - Fallecido" then 1 else 0 end) AS Fallecidos
FROM test_0
WHERE (residencia_provincia_nombre="CABA" AND residencia_departamento_nombre<>"SIN ESPECIFICAR")
GROUP BY residencia_departamento_nombre;

SELECT count(*) FROM test_0 WHERE (residencia_provincia_nombre="CABA" AND residencia_departamento_nombre<>"SIN ESPECIFICAR");
SELECT fecha_apertura, count(*) FROM test_0 WHERE (clasificacion_resumen="Confirmado") group by fecha_apertura  ORDER BY "fecha_apertura" DESC LIMIT 7;

SELECT * FROM test_0 WHERE (residencia_provincia_nombre="CABA");

SELECT * FROM test_0 WHERE (residencia_provincia_nombre="CABA" AND residencia_departamento_nombre<>"SIN ESPECIFICAR");