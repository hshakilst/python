#!/usr/bin/python

import sys
import getopt
import csv

admin = ['ADMIN-PC-01', 'ADMIN-PC-02', 'ADMIN-PC-03',
         'ADMIN-PC-04', 'ADMIN-PC-05', 'ADMIN-PC-06', 'ADMIN-PC-07']
executive = ['EXECUTIVE-PC-1', 'EXECUTIVE-PC-2', 'EXECUTIVE-PC-3', 'EXECUTIVE-PC-4', 'EXECUTIVE-PC-5', 'EXECUTIVE-PC-6', 'EXECUTIVE-PC-7', 'EXECUTIVE-PC-8', 'EXECUTIVE-PC-9', 'EXECUTIVE-PC-10', 'EXECUTIVE-PC-11', 'EXECUTIVE-PC-12', 'EXECUTIVE-PC-13',
             'EXECUTIVE-PC-14', 'EXECUTIVE-PC-15', 'EXECUTIVE-PC-16', 'EXECUTIVE-PC-17', 'EXECUTIVE-PC-18', 'EXECUTIVE-PC-19', 'EXECUTIVE-PC-20', 'EXECUTIVE-PC-21', 'EXECUTIVE-PC-22', 'EXECUTIVE-PC-23', 'EXECUTIVE-PC-24', 'EXECUTIVE-PC-25', 'EXECUTIVE-PC-26']
operational = ['OPERATIONAL-PC-1', 'OPERATIONAL-PC-2', 'OPERATIONAL-PC-3', 'OPERATIONAL-PC-4', 'OPERATIONAL-PC-5', 'OPERATIONAL-PC-6', 'OPERATIONAL-PC-7', 'OPERATIONAL-PC-8', 'OPERATIONAL-PC-9', 'OPERATIONAL-PC-10', 'OPERATIONAL-PC-11', 'OPERATIONAL-PC-12', 'OPERATIONAL-PC-13', 'OPERATIONAL-PC-14', 'OPERATIONAL-PC-15', 'OPERATIONAL-PC-16', 'OPERATIONAL-PC-17', 'OPERATIONAL-PC-18', 'OPERATIONAL-PC-19', 'OPERATIONAL-PC-20', 'OPERATIONAL-PC-21', 'OPERATIONAL-PC-22', 'OPERATIONAL-PC-23', 'OPERATIONAL-PC-24',
               'OPERATIONAL-PC-25', 'OPERATIONAL-PC-26', 'OPERATIONAL-PC-27', 'OPERATIONAL-PC-28', 'OPERATIONAL-PC-29', 'OPERATIONAL-PC-30', 'OPERATIONAL-PC-31', 'OPERATIONAL-PC-32', 'OPERATIONAL-PC-33', 'OPERATIONAL-PC-34', 'OPERATIONAL-PC-35', 'OPERATIONAL-PC-36', 'OPERATIONAL-PC-37', 'OPERATIONAL-PC-38', 'OPERATIONAL-PC-39', 'OPERATIONAL-PC-40', 'OPERATIONAL-PC-41', 'OPERATIONAL-PC-42', 'OPERATIONAL-PC-43', 'OPERATIONAL-PC-44', 'OPERATIONAL-PC-45', 'OPERATIONAL-PC-46', 'OPERATIONAL-PC-47', 'OPERATIONAL-PC-48', 'OPERATIONAL-PC-49']


def insertRow(fname):
    file = open(fname)
    reader = csv.reader(file, delimiter='\t')
    all=[]
    i = 0
    j = 0
    k = 0
    for item in reader:
        if (i < 7):
            item.append(admin[i])
            all.append(item)
            i+=1
        elif (j < 26):
            item.append(executive[j])
            all.append(item)
            j+=1
        elif (k < 49):
            item.append(operational[k])
            all.append(item)
            k+=1
    print all
    file = open(fname,'wb')
    writer = csv.writer(file, delimiter='\t')
    writer.writerows(all)
    


def main(argv):
    fname = ''
    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    except getopt.GetoptError:
        print 'csv.py -i <file file>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'csv.py -i <file file>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            fname = arg
    print 'file file is ', fname
    insertRow(fname)


if __name__ == "__main__":
    main(sys.argv[1:])
