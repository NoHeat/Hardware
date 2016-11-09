#!/usr/bin/env python

#Import for GPIO usage
import RPi.GPIO as GPIO
import csv
import os
import sys
import re
import base64
import hashlib
import hmac
import urllib2
import json
import struct
import select
import socket
import random
import smtplib
import sensval

from semantics3 import Products

# Set up a client to talk to the Semantics3 API using your Semantics3 API Credentials
sem3 = Products(
    api_key = "SEM310553EF475655749A2C9447BFDAFD50A",
    api_secret = "OGQ0YTYwNzdiZDgxMzEwNTVjMTdlMWZlYjY4ZDQ1Y2Y"
    )

items_path = "/root/Desktop/GitReps/Hardware/items.csv"

# append existing barcode scans to document to keep for record
def createcsv(a, b):
    with open(items_path, 'a') as upcFile:
        upcFileWriter = csv.writer(upcFile)
        upcFileWriter.writerow([a, b, "Amount", "H", "L", "E"])
        
# clear csv file after sent to the server
def clearcsv():
    with open(items_path, 'w'):
        pass
    
# calling the api using the UPCCODE which is what our parse scanner returned
def url_search(UPCCODE):
    # Build the request
    sem3.products_field("upc", UPCCODE)
    sem3.products_field("fields", ["name","category"])

    # Run the request
    answer = sem3.get_products()
    # print answer
    # View the results of the request
    # print just the name from the all the info retrieved on that barcode
    for item in answer['results']:
	# print item['name']
        return item['name']

def url_searchcat(UPCCODE):
    # Build the request
    sem3.products_field("upc", UPCCODE)
    sem3.products_field("fields", ["category"])

    # Run the request
    answer = sem3.get_products()
    # print answer
    # View the results of the request
    # print just the name from the all the info retrieved on that barcode
    for item in answer['results']:
	# print item['name']
        return item['category']

# translating the barcode info retrieved from the event folder into a UPC barcode
def parse_scanner_data(scanner_data):
    upc_chars = []
    for i in range(0, len(scanner_data), 16):
        chunk = scanner_data[i:i+16]

        # The chunks we care about will match
        # __  __  __  __  __  __  __  __  01  00  __  00  00  00  00  00
        if chunk[8:10] != '\x01\x00' or chunk[11:] != '\x00\x00\x00\x00\x00':
            continue

        digit_int = struct.unpack('>h', chunk[9:11])[0]
        upc_chars.append(str((digit_int - 1) % 10))

    return ''.join(upc_chars)


#Definition for scanner usage

def main():
    f = open('/dev/input/event0', 'rb')

    while not (sensval.analog_read() == 0):
        print 'Waiting for scanner data'
        # Wait for binary data from the scanner and then read it
        scan_complete = False
        scanner_data = ''

        while not (sensval.analog_read() == 0):
            rlist, _wlist, _elist = select.select([f], [], [], 0.1)
            if rlist != []:
                new_data = ''
                while not new_data.endswith('\x01\x00\x1c\x00\x01\x00\x00\x00'):
                    new_data = rlist[0].read(16)
                    scanner_data += new_data
                # There are 4 more keystrokes sent after the one we matched against,
                # so we flush out that buffer before proceeding:
                [rlist[0].read(16) for i in range(4)]

                scan_complete = True
            if scan_complete:
                barcode = parse_scanner_data(scanner_data)
                print "Scanned barcode '{0}'".format(barcode)
                itemresult = url_search(barcode)
		catresult = url_searchcat(barcode)
                print itemresult
		print catresult
            #checking for incorrect barcode scan
            #if (itemresult == 'None'):
                #break
            #else:
                createcsv(itemresult, catresult)
                break
    #clearcsv()    

if __name__ == "__main__":
    main()