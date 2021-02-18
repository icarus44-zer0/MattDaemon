#other peoples python 
import sys
import socket
import threading


class NetcatManager(object):
    def __init__(self, rhost, rport, timeout=0.1):
        self._event = threading.Event()
        self._socket = socket.create_connection((rhost, rport))
        self._socket.settimeout(timeout)

    def __enter__(self):
        self._reading_thread = threading.Thread(target=print_recv, args=(self._socket, self._event))
        self._reading_thread.start()
        return self._socket

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._event.set()
        # Waiting for thread termination so there is no OSError when closing the socket
        self._reading_thread.join()
        self._socket.close()


def print_recv(sock, event):
    while not event.is_set():
        try:
            msg = sock.recv(4096)
        except socket.timeout:
            pass
        else:
            if not msg:
                break
            sys.stdout.write(msg)
            sys.stdout.flush()


def netcat_session(rhost, rport, input_file=sys.stdin):
    with NetcatManager(rhost, rport) as netcat_socket:
        # We do not iterate (for line in input_file) because stdin does not behave well in Python 2
        while True:
            line = input_file.readline()
            if not line:
                # EOF reached
                break
            netcat_socket.sendall(line)
    # Leave with the screen in a clean state
    print