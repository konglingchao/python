#!/usr/bin/env python
#! _*_ coding utf-8 _*_

class MyClass():
    def __init__(self,name ="unset", color = "black"):
        print "constructor is called with parms:" ,name, "---",color
        self.__name = name 
        self.color = color 
    def __del__(self):
        print "Destructor is called for %s" % self.__name
 
inst= MyClass()
print inst.color
print inst.__name
