#!/usr/bin/python3

import sys, cv2, os, shutil
indir = '/home/nyk/nikon_696x464'
outdir = 'nikon_faces'
cascasdepath = "/home/nyk/Florologium/haarcascade_frontalface_default.xml"
if not os.path.isdir(outdir): os.mkdir(outdir)

def face_detect(imgpath):
    image = cv2.imread(imgpath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cascasdepath)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (20, 20))
    return len(faces)

for f in os.listdir(indir):
    fn1 = '%s/%s' % (indir, f)
    fn2 = '%s/%s' % (outdir, f)
    nbf = face_detect(fn1)
    if nbf > 1:
        shutil.copy(fn1, fn2)
        print('%s: %d' % (f, nbf))
