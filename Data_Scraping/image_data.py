#!/usr/bin/python
import Algorithmia, sys, getopt, json
from Algorithmia.acl import ReadAcl, AclType

client = Algorithmia.client("sim+6rq2ICve0w0GWRL3fBXTxLa1")

def init():
    nlp_directory = client.dir("data://hshakilst/nlp_directory")
    # Create your data collection if it does not exist
    if nlp_directory.exists() is False:
	    nlp_directory.create()

    acl = nlp_directory.get_permissions()  # Acl object
    acl.read_acl == AclType.my_algos  # True

    # Update permissions to private
    nlp_directory.update_permissions(ReadAcl.private)
    nlp_directory.get_permissions().read_acl == AclType.private # True

def uploadFile(fname):
    file = "data://hshakilst/nlp_directory/"+fname
    if client.file(file).exists() is False:
	    client.file(file).putFile(fname)
    return file


def analyze(url):
    image = url

    tagger1 = client.algo("deeplearning/IllustrationTagger/0.2.5")
    tagger2 = client.algo("deeplearning/InceptionNet/1.0.3")
    tagger3 = client.algo("character_recognition/SmartTextExtraction/0.1.1")
    tagger4 = client.algo("deeplearning/ObjectDetectionCOCO/0.2.1")

    print "IllustrationTagger:", json.dumps(tagger1.pipe({"image": image}).result, sort_keys=True, indent=4)
    print "InceptionNet:", json.dumps(tagger2.pipe(image).result, sort_keys=True, indent=4)
    print "OCR:", json.dumps(tagger3.pipe({"image": image, "language": "eng"}).result, sort_keys=True, indent=4)
    input = {
        "image": image,
        "min_score": 0.7,
        "model": "ssd_mobilenet_v1"
    }
    print "COCO(Object Detection):", json.dumps(tagger4.pipe(input).result, sort_keys=True, indent=4)

def deleteFile(url):
    if client.file(url).exists() is True:
        client.file(url).delete()

def main(argv):
    fname = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print 'image_data.py -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'image_data.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            fname = arg
    print 'Input file is ', fname
    init()
    url = uploadFile(fname)
    analyze(url)
    deleteFile(url)

if __name__ == "__main__":
    main(sys.argv[1:])