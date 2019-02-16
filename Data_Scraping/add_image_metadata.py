#!/usr/bin/python

import sys
import getopt
import csv
import glob
import pyexiv2
import json

#************************************Important note********************************
#No. of files will be multiplied by 7 like if we input 3 no. of files will be 7*3=21 (for admin.tsv)
#No. of files will be multiplied by 26 like if we input 3 no. of files will be 26*3=78 (for admin.tsv)
#No. of files will be multiplied by 49 like if we input 3 no. of files will be 49*3=147 (for admin.tsv)

def add_metadata(fname, num_of_files):
    file = open(fname)
    reader = csv.reader(file, delimiter='\t')
    img_list = glob.glob("./images/*.jpg")
    n = int(num_of_files)
    i = 0
    j = 0
    while(j < n):
        for row in reader:
            metadata = pyexiv2.ImageMetadata(img_list[i])
            metadata.read()
            userdata = {'Author': row[0] + " " + row[1], 'Email': row[2],
                    'ComputerName': row[3], 'Tagged': 'Yes'}
            metadata['Exif.Photo.UserComment']=json.dumps(userdata)
            metadata.write()
            print str(i) + '. ' + (img_list[i].split('/'))[2]
            i+=1
        file.seek(0)
        j+=1
    file.close()
        
def main(argv):
    fname = ''
    try:
        opts, args = getopt.getopt(argv, "hi:n:", ["ifile=", "num_of_files="])
    except getopt.GetoptError:
        print 'add_image_metadata.py -i <input file> -n <number of files>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'add_image_metadata.py -i <input file> -n <number of files>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            fname = arg
        elif opt in ("-n", "--num_of_files"):
            num_of_files = arg
    print 'Input file is ', fname
    print 'Number of file is', num_of_files
    add_metadata(fname, num_of_files)

if __name__ == "__main__":
    main(sys.argv[1:])
