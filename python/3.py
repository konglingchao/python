#!/usr/bin/env python2.6
# _*_ coding: utf-8 _*_

import datetime

def nameFunc(a):
    return "I'm nead function with param %s " % a

def call_func(func,param):
    print datetime.datetime.now()
    print func(param)
    print ""

if __name__ == "__main__":
    call_func(nameFunc,"hello")
