import argparse
import sys
parser = argparse.ArgumentParser(prog=sys.argv[0],description="a test file to learn some modules")
parser.add_argument("-vd", default='C:\\Users\\Alex\\Desktop\\opencv-3.4\\opencv-3.4\\samples\\data\\vtest.avi', help='address of video in string', type=str)
args = parser.parse_args()

capture = cv.VideoCapture(cv.samples.findFilesOrKeep(args.vd))
print(sys.version_info)

