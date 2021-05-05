import sys
import socket
import signal
import time
import math

SERVER_PORT = 8080
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

def server(duration):
    # Attempt to open a socket
    socket.setdefaulttimeout(duration)
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as error:
        sys.exit("Failed to open socket: Error: " + str(error))

    # Attempt to bind socket
    try:
        sock.bind(('', SERVER_PORT))
    except socket.error as error:
        sys.exit("Failed to bind socket: Error: " + str(error))

    # Attempt to listen to socket
    try:
        sock.listen(QUEUE_LENGTH)
    except socket.error as error:
        sys.exit("Failed to bind socket: Error: " + str(error))

    # Infinitely accept connections and log their results

    total = 0

    try:
        # Accept incoming connection from 'address'
        conn, addr = sock.accept()
        start_time = time.time()
        end_time = start_time
        while end_time < start_time + duration:
            data = conn.recv(RECV_BUFFER_SIZE)
            if not data:
                break
            total += len(data)
            end_time = time.time()
        sys.stdout.flush()
        conn.close()
    except socket.error as error:
        pass
    except IOError as error:
        sys.exit("Failed to write to log file: " + str(error))

    print(str(math.floor(total/1000/duration)))

def main():
    # Register signal handlers
    signal.signal(signal.SIGINT, signalHandler)
    signal.signal(signal.SIGTERM, signalHandler)

    # Parse command line arguments and run server
    if len(sys.argv) != 2:
        sys.exit("Usage: python honest-receiver.py (DURATION)")
    duration = int(sys.argv[1])
    server(duration)

if __name__ == "__main__":
    main()
