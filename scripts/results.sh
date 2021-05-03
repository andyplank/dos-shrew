#!/bin/bash

counter=400
while [[ $counter -le 5000 ]]
do
        ./attack $counter 200 10 5
        counter=$((counter + 100))
done

rm cli.sh
