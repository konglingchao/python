#!/usr/bin/env python2.6
# _*_ coding: utf-8 _*_

class MyClass(object):
    message = "Hello, Developer"

    def show(self):
        print self.message

    def __init__(self,name = "unset",color = "black"):
        print "Contructor is called with params:" ,name, "",  color

    def __del__(self):
        print "Destructor is called"
 
inst = MyClass()
inst.show()
del inst
inst2 = MyClass("David")
inst2.show()

