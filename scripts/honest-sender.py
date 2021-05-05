import sys
import socket
import os

SEND_BUFFER_SIZE = 1400

def sendtodst(server_ip, server_port): 
    # Attempt to open a socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as error:
        sys.exit("Failed to open socket: Error: " + str(error))

    # Attempt to connect to server
    try:
        sock.connect((server_ip, server_port))
    except socket.error as error:
        sys.exit("Failed to connect socket to end host: Error: " + str(error))

    # Infinitely send TCP traffic to the designated recipient
    try:
        while True:
            sock.send(bytearray(SEND_BUFFER_SIZE))
    except socket.error as error:
        sys.exit("Failed to send data to server. Error: " + str(error))
    # Communication succeeded.

def main():
    """Parse command-line arguments and call client function """
    if len(sys.argv) != 3:
        sys.exit("Usage: python honest-sender.py (Server IP) (Server Port)")
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    sendtodst(server_ip, server_port)

if __name__ == "__main__":
    main()
