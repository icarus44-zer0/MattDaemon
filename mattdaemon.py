# run a netcat and log the results
# graciously barrowed 
# https://www.instructables.com/Netcat-in-Python/


import sys
import socket
import time
import pandas as pd 
import threading


# TODO Build Loop for all comon Ports then random ports 
# TODO Network Crawler access local Gateway 
# TODO Network Crawler find first hop Router  
# TODO Lateral LAN and VLAN Crawling   
# TODO Log identified box
# TODO port scan identified boxs 
# TODO Store returned port data into data frame 

def netcat(targetAddr,targetPort,content):
    # create connection over tcp 
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        sock.connect((targetAddr,targetPort))
        #send all content over the socket 
        sock.sendall(content)
        time.sleep(.5)
        sock.shutdown(socket.SHUT_WR)

        #read the result of the connection into a buffer
        serResponce = None
        
        while (True):
            try:
                data = sock.recv(1024)
                if(not data):
                    break
                serResponce = data.decode()
            except:
                print("No Resonce on Port: " + str(targetPort))
                break

        if (serResponce):
            print("server responce: " + serResponce)
        sock.close()
    except:
        print("Connection Refused on port" + str(targetPort))
        pass

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

# main fucntion configure ports and scan
def main(): 
    targetAddr = "192.168.1.237"
    targetPort = 8000
    content = bytes("", "UTF-8")

    while (targetPort<8001):
        content = bytes("", "UTF-8")
        content2 = bytes("HEAD / HTTP/1.1\nHost:" + str(targetAddr) +"\n" +"END\nHTTP/1.0 200 OK\n", "UTF-8")
        netcat(targetAddr,targetPort,content2)
        targetPort+=1

if __name__ == "__main__":
    # execute only if run as a script
    main()