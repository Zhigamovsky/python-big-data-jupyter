#!/usr/bin/env bash

set -u;

docker-compose down
docker-compose build zhigamovsky_python_jupyter
docker-compose up -d zhigamovsky_python_jupyter
