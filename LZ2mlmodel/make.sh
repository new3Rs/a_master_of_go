#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: make.sh <URL>"
    exit 1
fi
pipenv install
pipenv shell URL=$1 make