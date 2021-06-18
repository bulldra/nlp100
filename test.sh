#!/bin/bash

if [ $# == 1 ]; then
    TEST_PATH="./tests/$1"
else
    TEST_PATH="./tests/"
fi
docker-compose run --entrypoint "pytest -s $TEST_PATH" nlp100
docker-compose down
