#!/usr/bin/env python
#! _*_ coding: utf-8 _*_

class Base(object):
    def __init__(self):
        print "def __init__(self):"
    def __del__(self):
        print "Destructor of Base is called!"
    def move(self):
        print "MOVE CALLED IN base!" 

class SubA(Base):
    def __init__(self):
        print "constructor of SUBA is called"
    def move(self):
        print "move called in subA"

class SubB(Base):
    def __del__(self):
        print " constructor of SUBB is called"
        super(SubB,self).__del__()  
    
instA = SubA()
instA.move()
del instA

print "*"*50


instB= SubB()
instB.move()
