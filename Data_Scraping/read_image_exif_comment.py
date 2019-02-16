#!/usr/bin/python
import sys, getopt
import json
import pyexiv2
import glob

def read_EXIF_comment(fname):
    metadata = pyexiv2.ImageMetadata(fname)
    metadata.read()
    # for key in metadata.keys():
    #     print key + ': ' + str(metadata[key].value)
    userdata=json.loads(metadata['Exif.Photo.UserComment'].value)
    print fname +':\n'+ json.dumps(userdata, sort_keys=True, indent=4)


def main(argv):
    fname = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print 'read_image_exif_comment.py -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'read_image_exif_comment.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            fname = arg
    print 'Input file is "', fname
    read_EXIF_comment(fname)

if __name__ == "__main__":
    main(sys.argv[1:])

# def main():
#     list = glob.glob("./images/*.jpg")
#     file = open("images_metadata.txt", "wb")
#     i = 1
#     for img in list:
#         file.write(read_EXIF_comment(img))
#         file.writelines('\n')
#         print str(i) + '. ', (img.split('/'))[2]
#         i+=1
#     file.close()

# main()