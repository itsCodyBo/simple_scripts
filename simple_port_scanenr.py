#!/usr/bin/env python

#__author__: jack
# visit digitz.org

#Importing the modules
#socket = used to make a socket connection
#argparse is used to parse arguments
import socket, sys, time, datetime, argparse, os
flag = 0 #we will come back to this flag later
os.system('clear') #clear the console

#fancy banner
line = '+' * 80
desc = line+ "'\nA Simple port scanner that works!!"

#reminder: look up 'argparse' later and parsing arguments
parser = argparse.ArgumentParser(description=desc, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('host',metavar='H',help='Host name you want to scan')
parser.add_argument('startport',metavar='P1' , nargs='?',help='Start scanning from this port')
parser.add_argument('endport',metavar='P2',nargs='?',help='Scan until this port')
args = parser.parse_args()

host = args.host #The host name to scan for open ports
ip = socket.gethostbyname(host) #Converts the host name into IP address

#args.startpoint corresponds to the first port we will scan
#args.endport corresponds to the last port

