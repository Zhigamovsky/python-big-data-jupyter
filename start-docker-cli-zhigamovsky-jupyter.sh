#!/usr/bin/env bash

set -u;

docker build -f Dockerfile.zhigamovsky_python_jupyter -t zhigamovsky_python_jupyter:latest .
docker run -d --rm --name zhigamovsky_python_jupyter -p 8888:8888 -v $PWD:/app zhigamovsky_python_jupyter:latest
