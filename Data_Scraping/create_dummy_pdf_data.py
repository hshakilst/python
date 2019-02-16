#!/usr/bin/python

import sys
import getopt
import pdfkit
import random
import string
import time


def random_key(length):
    key = ''
    for i in range(length):
        key += random.choice(string.lowercase +
                             string.uppercase + string.digits)
    return key


def createPdf(fname):
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
    }
    file = open(fname)
    urls = file.readlines()
    for url in urls:
        try:
            pdfkit.from_url(url.strip(), './pdfs/' + random_key(8)+ '.pdf', options=options)
            time.sleep(5)
        except:
            continue
    file.close()


def main(argv):
    fname = ''		#file containing urls each one in a line
    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    except getopt.GetoptError:
        print 'create_dummy_pdf_data.py -i <urls>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'create_dummy_pdf_data.py -i <urls.txt>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            fname = arg
    print 'Input file is ', fname
    createPdf(fname)

if __name__ == "__main__":
    main(sys.argv[1:])
