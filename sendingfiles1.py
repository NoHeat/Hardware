#!/usr/bin/env python
#recieving pi code (client)
import socket
import sys
import time

HOST = '192.168.1.225'    # The remote host
PORT = 4321              # The same port as used by the server
def main (path):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #create new socket using the given address family
	s.connect((HOST, PORT))   #connect to the remote socket above
	f = open(path, 'rb')  #open the file sent from above, file name can change
	l = f.read(1)    #read the file opened
	
	while (l):
	    s.send(l)   #send recieved flag to server
	    l = f.read(1)    #read the file opened
	f.close()
	s.shutdown(socket.SHUT_WR)
	print s.recv(1)
	s.close()
	time.sleep(1)
## wait for no fucking reason

if __name__ == "__main__":
    main()
