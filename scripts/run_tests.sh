#!/bin/bash
[ -d "./data" ] && rm -rf ./data
mkdir data
sudo mn -c

counter=400
while [[ $counter -le 5000 ]]
do
        ./attack.sh $counter 200 10 5
        counter=$((counter + 100))
done

