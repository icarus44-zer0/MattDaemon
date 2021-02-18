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

def netcat(hn,p):
    # create connection over tcp 
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        sock.connect((hn,p))
        #send all content over the socket 
        content = bytes("", "UTF-8")
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
                print("No Resonce on Port: " + str(p))
                break

        if (serResponce):
            print("server responce: " + serResponce)
        sock.close()
    except:
        print("Connection Refused on port" + str(p))
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
    targetPort = 22

    while (targetPort):
        netcat(targetAddr,targetPort)
        targetPort+=1


if __name__ == "__main__":
    # execute only if run as a script
    main()

# i = 0
# while (i < 23):
#     netcat(targetAddr,i,content)
#     i+=1

 # commands to hit with bash scripts 
 
 # Active service 
    # systemctl list-units --type=service

    # Net Cat 
    # nc -v -n 8.8.8.8 1-1000