#!/bin/bash

declare -a dirs=(service1 service2 service3 service4)

for dir in ${dirs[@]}; do
    cd ${dir}
    pip3 install -r requirements.txt
    python3 -m pytest --cov --cov-report term-missing
    cd ..
done