$Sample = Get-Random -Minimum -100 -Maximum 100
#$Sample2 = New-Guid
#echo $Sample2
#  docker build -t myimage .
docker build --pull --no-cache --rm -f "Dockerfile" -t covidargentina:latest "."
docker run -i -t -d -p 3306:3306 --pid=host -v /var/lib/mysql --name covidargentina_container-$Sample covidargentina:latest
docker inspect --format '{{ .NetworkSettings.IPAddress }}' covidargentina_container-$Sample