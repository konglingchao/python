#!/usr/bin/env python
#! _*_ coding: utf-8 _*_

import socket
HOST='0.0.0.0'
PORT=3434
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((HOST,PORT))
while True:
    info,addr = s.recvfrom(1024)
    print "Received: %s from %s" % (info,str(addr))

s.close()
