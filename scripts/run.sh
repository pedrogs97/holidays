#!/bin/bash

docker build . -t holiday
{ # try
    docker network create --driver=bridge main
} || { # catch
    echo "network ok"
}
docker run -d --name=holidays --net=main -p 8000:8000 --hostname=holiday holiday
