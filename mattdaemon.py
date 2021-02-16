# run a netcat and log the results
import sys
import socket
import time

hostname = "192.168.1.1"
port = 80

def netcat(hn,p,content):
    # create connection over tcp 
    connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connection.connect((hn,p))

    #send all content over the socket 
    connection.sendall(content)
    time.sleep(.5)
    connection.shutdown(socket.SHUT_WR)

    #read the result of the connection into a buffer
    serResponce = ""

    while (True):
        data = connection.recv(1024)
        if(not data):
            break
        serResponce = data.decode()
    

    print(serResponce)
    print("\n Connection Closed \n")


    connection.close()

content = "GET / HTTP/1.1\nHost: google.com\n\n"
netcat(hostname, port, content.encode())

 