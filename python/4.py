#/usr/bin/env python2.6
# _*_ coding: utf-8 _*_

try:
    result = [2,10]
    print result[10]
    print "This is never been called"
except (IndexError,EOFError),e:
    print "Exception happened"
    print e
else:
    print "very good"
finally:
    print "Process finished"

