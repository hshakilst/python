#!/usr/bin/python
from file_metadata.generic_file import GenericFile
import spacy, sys, getopt, json, glob


def extractMetadata(fname):
    file = GenericFile.create(fname)
    res = json.dumps(file.analyze(), sort_keys=True, indent=4)
    print res



def main(argv):
    fname = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print 'metadata_extractor.py -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'metadata_extractor.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            fname = arg
    print 'Input file is "', fname
    extractMetadata(fname)

if __name__ == "__main__":
    main(sys.argv[1:])

        
