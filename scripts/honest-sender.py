import sys
import socket
import os

SERVER_PORT = 8080
SEND_BUFFER_SIZE = 1400

def sendtodst(server_ip): 
    # Attempt to open a socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as error:
        sys.exit("Failed to open socket: Error: " + str(error))

    # Attempt to connect to server
    try:
        sock.connect((server_ip, SERVER_PORT))
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
    if len(sys.argv) != 2:
        sys.exit("Usage: python honest-sender.py (Server IP)")
    server_ip = sys.argv[1]
    sendtodst(server_ip)

if __name__ == "__main__":
    main()
