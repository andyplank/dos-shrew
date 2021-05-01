build:
	sudo python3 buildnet.py

connect:
	h2 python3 honest-receiver.py 5000 &
	h1 python3 honest-sender.py 10.0.0.2 5000 &

attack:
	h3 python3 malicious-sender.py 10.0.0.2 5000 &
