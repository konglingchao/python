#!/usr/bin/env python
#! _*_ coding: utf-8 _*_
import socket
HOST='127.0.0.1'
PORT=3434
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
info = "HI,Konglingchao "
s.sendto(info,(HOST,PORT))
print "Send : %s to %s:%d" % (info,HOST,PORT)
s.close()

