#$Sample = Get-Random -Minimum -100 -Maximum 100
#$Sample2 = New-Guid
#echo $Sample2
docker build --pull --no-cache --rm -f "mysql.dockerfile" -t pythonmysql:latest "."
docker run -i -t -d -p 3306:3306 -p 5000:5000 --pid=host -v /var/lib/mysql --name pythonmysql pythonmysql:latest
docker inspect --format '{{ .NetworkSettings.IPAddress }}' pythonmysql