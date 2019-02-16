#!/usr/bin/python

import sys
import getopt
import random
import string
import time
import urllib2
import pypandoc


def random_key(length):
    key = ''
    for i in range(length):
        key += random.choice(string.lowercase +
                             string.uppercase + string.digits)
    return key


def createDoc(fname):
    file = open(fname)
    urls = file.readlines()
    for url in urls:
        try:
            response = urllib2.urlopen(url)
            time.sleep(5)
            content = response.read()
            pypandoc.convert(source=content, format='html', to='docx', outputfile='./docs/' + random_key(8)+ '.docx', extra_args=['-RTS'])  
        except:
            continue
    file.close()



def main(argv):
    fname = ''    #file containing urls each one in a line
    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    except getopt.GetoptError:
        print 'create_dummy_doc_data.py -i <urls>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'create_dummy_doc_data.py -i <urls.txt>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            fname = arg
    print 'Input file is ', fname
    createDoc(fname)

if __name__ == "__main__":
    main(sys.argv[1:])
