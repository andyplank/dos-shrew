#!/bin/bash
if [[ $# -ne 2 ]]; then 
    echo "./gen.sh <BURST_LENGTH> <TEST_DURATION>"
    exit 1
fi

[ -f "res.txt" ] && rm res.txt
touch res.txt
sudo mn -c

duration=$2
burst=$1
counter=400
while [[ $counter -le 5000 ]]
do
    echo "-----------------------------------------------------------------"
    echo " DoS Shrew - Square wave of $counter ms with burst duration of $burst ms"
    echo "-----------------------------------------------------------------"
    echo "h2 python3 honest-receiver.py $duration >> res.txt &" > cli.sh
    echo "h1 python3 honest-sender.py 10.0.0.2 &" >> cli.sh
    echo "h3 python3 malicious-sender.py 10.0.0.2 5000 $counter $burst &" >> cli.sh
    echo "h2 wait" >> cli.sh
    echo "quit" >> cli.sh
    echo "$counter $burst" >> res.txt
    sudo python3 buildnet.py
    counter=$((counter + 100))
done
python3 plot.py
