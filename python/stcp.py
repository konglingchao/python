#!/usr/bin/env python
#! _*_ coding: utf-8 _*_

import socket
import datetime

HOST='0.0.0.0'
PORT=3434
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

while True:
    conn,addr=s.accept()
    print 'Client %s connected' % str(addr)
    dt= datetime.datetime.now()
    data = "now time is %s" % str(dt)
    conn.send(data)
    print "Sent:", data
    conn.close()


