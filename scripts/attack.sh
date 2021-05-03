if [[ $# -ne 4 ]]; then 
        echo "./attack.sh <ATTACK_PERIOD_MS> <ATTACK_BURST_DURATION_MS> <TEST_DURATION_S> <LOG_INTERVAL_S>"
        exit 1
fi

# 2 second buffer to let iperf3 save data
total=$(($3+2))
echo "-----------------------------------------------------------------"
echo " DoS Shrew - Square wave of $1ms with burst duration of $2ms"
echo " Test Duration : $3s"
echo "-----------------------------------------------------------------"
echo "h2 iperf3 -s &" > cli.sh
echo "h1 iperf3 -c 10.0.0.2 -t $3 -i $4 -C reno -J > ./data/$1.json &" >> cli.sh
echo "h3 python3 malicious-sender.py 10.0.0.2 5000 $1 $2 &" >> cli.sh
echo "h1 sleep $total" >> cli.sh
echo "quit" >> cli.sh
sudo python3 buildnet.py
rm cli.sh
