from optparse import OptionParser  
parser = OptionParser()  
parser.add_option("-f", "--file", dest="filename",  
                  help="write report to FILE", metavar="FILE")  
  
(options, args) = parser.parse_args()  

