#!/usr/bin/env python
#code to send file thru sockets
#sending pi code (server)
import socket
import sys

HOST = '10.0.0.186'                 # Symbolic name meaning all available interfaces
PORT = 50002              # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create new socket using the given address family
s.bind((HOST,PORT))  #bind the socket to the address
print "before listen"
s.listen(10)    #set maximum accept rate to 10 connections
print "listen"

while(1):
    
    while True:
        print "Waiting for items.csv"
        sc, address = s.accept()    #accept a connection
        print "Accepted items.csv"
        f = open('/home/pi/Desktop/items.csv', 'wb')   #open in binary
        while True:
            l = sc.recv(1024)   #receive data from the socket
            while (l):	
                f.write(l)  #writes the contents of string to file
                l = sc.recv(1024)   #recieve data from socket again	    
            f.close()   #close the file opened from the function f
            sc.close()  #close sc from function
            break
        break

    while True:
        print "Waiting for top image"
        sc, address = s.accept()    #accept a connection
        print "Accepted top image"
        f = open('/home/pi/Desktop/capture_top.jpg', 'wb')   #open in binary
        while True:
            l = sc.recv(1024)   #receive data from the socket
            while (l):
                f.write(l)  #writes the contents of string to file
                l = sc.recv(1024)   #recieve data from socket again     
            f.close()   #close the file opened from the function f
            sc.close()  #close sc from function
            break
        break

    while True:
        print "Waiting for middle image"
        sc, address = s.accept()    #accept a connection
        print "Accepted middle image"
        f = open('/home/pi/Desktop/capture_mid.jpg', 'wb')   #open in binary
        while True:
            l = sc.recv(1024)   #receive data from the socket
            while (l):
                f.write(l)  #writes the contents of string to file
                l = sc.recv(1024)   #recieve data from socket again     
            f.close()   #close the file opened from the function f
            sc.close()  #close sc from function
            break
        break

    while True:
        print "Waiting for bottom image"
        sc, address = s.accept()    #accept a connection
        print "Accepted bottom image"
        f = open('/home/pi/Desktop/capture_low.jpg', 'wb')   #open in binary
        while True:
            l = sc.recv(1024)   #receive data from the socket
            while (l):
                f.write(l)  #writes the contents of string to file
                l = sc.recv(1024)   #recieve data from socket again     
            f.close()   #close the file opened from the function f
            sc.close()  #close sc from function
            break
        break



