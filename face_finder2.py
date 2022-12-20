#!/usr/bin/python3
# sudo pip3 install face_recognition

import sys, face_recognition, os, shutil
#indir = '/home/nyk/nikon_696x464'
indir = '/home/nyk/nikon_348x232'
outdir = 'nikon_faces'
if not os.path.isdir(outdir): os.mkdir(outdir)

def face_detect(imgpath):
    image = face_recognition.load_image_file(imgpath)
    faces = face_recognition.face_locations(image, number_of_times_to_upsample=2, model="cnn")
    return len(faces)

for f in sorted(os.listdir(indir)):
    fn1 = '%s/%s' % (indir, f)
    fn2 = '%s/%s' % (outdir, f)
    nbf = face_detect(fn1)
    print('%s: %d' % (f, nbf))
    if nbf > 0: shutil.copy(fn1, fn2)
        
