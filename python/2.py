#!/usr/bin/env python2.6
# _*_ coding: utf-8 _*_
 
def check_book(**dictParam):
    if dictParam.has_key['Price']:
        price = int(dictParam['Price'])
        if price > 100:
           print "*******I want buy this book!*********"
    print " The book information are as follow:"
    for key in dictParam.keys():
        print key,": ", dcitParam[key]
    print ""

if __name__ == "__main__":
    check_book(author = 'jems', Title='`konglingchao', Price = 105)
