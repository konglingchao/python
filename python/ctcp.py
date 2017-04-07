#!/usr/bin/env python2.6
#! _*_ coding: utf-8 _*_
import socket
HOST = '127.0.0.1'
PORT = 3434
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
print "connet %s %d ok" % (HOST,PORT)
data = s.recv(1024)
print "Received:",data
s.close()
