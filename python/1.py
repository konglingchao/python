#!/usr/bin/env python2.6
# _*_  coding: utf-8 _*_

import time

def fbis(num):
    result=[0,1]
    for i in range(num):
        result.append(result[-2]+result[-1])
    return  result

def main():
    result = fbis(10) 
    fobj = open('/Users/konglingchao/result.txt','w+')
    for i,num in enumerate(result):
        print u"第 %d 个数是 %d " % (i,num)
        fobj.write("%d"%num)
        time.sleep(1)

if __name__ == '__main__':
    main()
        
