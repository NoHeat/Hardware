#!/usr/bin/env python
#recieving pi code (client)
import socket
import sys
import time

HOST = '192.168.1.225'    # The remote host
PORT = 1234              # The same port as used by the server
def main ():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #create new socket using the given address family
	s.connect((HOST, PORT))   #connect to the remote socket above
	s.send('1')   #send recieved flag to server
	s.shutdown(socket.SHUT_WR)
	s.close()
	time.sleep(1)
## wait for no fucking reason

if __name__ == "__main__":
    main()
