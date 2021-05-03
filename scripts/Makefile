build:
	sudo python3 buildnet.py

receiver:
	iperf3 -s &

sender:
	iperf3 -c 10.0.0.2 -t 45 -i 5 -C reno

attack:
	python3 malicious-sender.py 10.0.0.2 5000 40 2 &
