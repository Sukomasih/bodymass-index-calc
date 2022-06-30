# Instruction running docker compose service
## Install docker
- Install docker : [link](https://docs.docker.com/engine/install/) \
just skip it, if docker already exists

## Running service
- `cd docker-compose-file`
- `docker network create tools` \
Create network for monitoring tools service
- `docker compose -f docker-compose-monitoring.yaml up -d` \
Running service loki, prometheus, grafana, docker exporter, and blackbox exporter
- `docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions` \
Install logging driver loki in docker
- `docker plugin ls` \
Check status logging driver, after install driver
- `export TAG=v0.1.5` \
Add variable tag in env OS for use docker-compose pull images
- `docker compose -f docker-compose.yaml up -d` \
Running BMI calculator service

## Test
- BMI url
> http://localhost/?height=170&weight=50
- Monitoring tools (Grafana) 
> Url : http://localhost:3000 \
> User : admin \
> Pass : admin \
> Just default credential access