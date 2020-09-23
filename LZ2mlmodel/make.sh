#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: make.sh <SIZE> <URL>"
    exit 1
fi
pipenv sync
pipenv shell SIZE=$1 URL=$2 make