#!/usr/bin/env python2.6
# _*_ coding: utf-8 _*_

import sys

class MyError(Exception):
    def __str__(self):
        return  "I'm a self-defiend Error!"

   
def main():
    try:
        print "***********Start of main()*************"
        if len(sys.argv)== 1:
           raise MyError()
        print "***********End of main()***************"
    except MyError, e:
        print e

if __name__ == '__main__':
    main()
