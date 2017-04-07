#!/usr/bin/env python2.6
# _*_ coding: utf-8 _*_

class MyClass(object):
    message = " Hello, Developer"
   
    def show(self):
        print self.message
        print "Here is %s in %s !" % (self.name,self.color)
  
    @staticmethod
    def printMessage():
        print "pinrt statimethod"
        print MyClass.message

    @classmethod
    def createobj(cls,name,color):
        print "object will be created:  %s  and" % (name)
        return cls(name,color)
  
    def __init__(self,name = "unset", color = "black"):
        print "---",name, "--",color
        self.name = name 
        self.color = color


MyClass.printMessage()
inst=MyClass.createobj('reda','ko')
