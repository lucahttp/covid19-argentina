/*
SELECT * CONVERT(datetime,fecha_apertura);
ALTER TABLE test_0 MODIFY fecha_apertura datetime;
ALTER TABLE test_0 CHANGE fecha_apertura datetime;
, "sepi_apertura" DESC, "fecha_apertura" ASC


SELECT * FROM "main"."test_0" ORDER BY "fecha_apertura" DESC LIMIT 1000;

SELECT fecha_apertura, count(*) FROM test_0 WHERE (clasificacion_resumen="Confirmado") group by fecha_apertura  ORDER BY "fecha_apertura" DESC LIMIT 7;
*/

DROP TABLE IF EXISTS test_0;
