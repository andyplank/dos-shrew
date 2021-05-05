import sys
import socket
import signal
import os
import time

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10
sock = None
conn = None

def signalHandler(signalNumber, frame):
    if(conn != None ):
        close(conn)

    if (sock != None):
        close(sock)
    
    sys.exit()

def server(server_port):
    # Attempt to open a socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as error:
        sys.exit("Failed to open socket: Error: " + str(error))

    # Attempt to bind socket
    try:
        sock.bind(('', server_port))
    except socket.error as error:
        sys.exit("Failed to bind socket: Error: " + str(error))

    # Attempt to listen to socket
    try:
        sock.listen(QUEUE_LENGTH)
    except socket.error as error:
        sys.exit("Failed to bind socket: Error: " + str(error))

    # Infinitely accept connections and log their results

    try:
        # Accept incoming connection from 'address'
        conn, addr = sock.accept()
        start_time = time.time()
        end_time = start_time
        total = 0
        while end_time < start_time + 30:
            data = conn.recv(RECV_BUFFER_SIZE)
            if not data:
                break
            total += len(data)
            end_time = time.time()
        print(str(round(total/1000/(end_time-start_time),2)) + "KBps")
        sys.stdout.flush()
        conn.close()
    except socket.error as error:
        pass
    except IOError as error:
        sys.exit("Failed to write to log file: " + str(error))
            

def main():
    # Register signal handlers
    signal.signal(signal.SIGINT, signalHandler)
    signal.signal(signal.SIGTERM, signalHandler)

    # Parse command line arguments and run server
    if len(sys.argv) != 2:
        sys.exit("Usage: python honest-receiver.py (Server Port)")
    server_port = int(sys.argv[1])
    server(server_port)

if __name__ == "__main__":
    main()
