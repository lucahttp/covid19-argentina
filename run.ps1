#$Sample = Get-Random -Minimum -100 -Maximum 100
#$Sample2 = New-Guid
#echo $Sample2
#  docker build -t myimage .

#docker build --rm -f "Dockerfile" -t covidargentina:latest "."
docker build --pull --no-cache --rm -f "Dockerfile" -t covidargentina:latest "."

#docker run -i -t -d -p 5000:5000 --name covidargentina_container-$Sample covidargentina:latest
#docker inspect --format '{{ .NetworkSettings.IPAddress }}' covidargentina_container-$Sample
docker run -i -t -d -p 5000:5000 --name covidargentina covidargentina:latest

docker inspect --format '{{ .NetworkSettings.IPAddress }}' covidargentina


# docker run -i -t -d  -p 5000:5000 --name covidargentina myimage:latest