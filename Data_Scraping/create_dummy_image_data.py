#!/usr/bin/python

import sys
import getopt
import random
import string
import time
import urllib2
import csv


def random_key(length):
    key = ''
    for i in range(length):
        key += random.choice(string.lowercase +
                             string.uppercase + string.digits)
    return key


def createImage(fname):
    tsvfile = open(fname)
    count = 0
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
        try:
            if count != 500:
                response = urllib2.urlopen(row[0])
                if response.getcode() == 200:
                    image = response.read()
                    file = open('./images/'+ random_key(8) +'.jpg','wb')
                    file.write(image)
                    file.close()
                    count += 1
                    print str(count) + '. '+file.name
            else:
                break   
        except:
            continue
    file.close()
        



def main(argv):
    fname = ''		#file containing urls each one in a line
    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    except getopt.GetoptError:
        print 'create_dummy_image_data.py -i <urls>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'create_dummy_image_data.py -i <urls.txt>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            fname = arg
    print 'Input file is ', fname
    createImage(fname)

if __name__ == "__main__":
    main(sys.argv[1:])
