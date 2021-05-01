build:
	sudo python3 buildnet.py

receiver:
	python3 honest-receiver.py 5000 &

sender:
	python3 honest-sender.py 10.0.0.2 5000 &

attack:
	python3 malicious-sender.py 10.0.0.2 5000 &
