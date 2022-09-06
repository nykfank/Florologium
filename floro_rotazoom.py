#!/usr/bin/python3
# Rotating zoom timelapse
# 2010-06-21 by Nick Fankhauser
# 2014-03-24: simplified
# 2020-08-22: Adapted to python3
import sys,os,time,PIL.Image,math,numpy,subprocess

framerate = 20
wink = math.pi / 2
wink = math.pi 
dvdx,dvdy = 2048, 1080 # target resolution (DVD: 720,576)
starttime=time.time()
startDir=os.path.abspath(sys.argv[1]).rstrip('/')+'/'
tDir = '%s_rota' % startDir.rstrip('/')
mfn = 'timelapse2K/%s_rota.mp4' % startDir.rstrip('/')

def clean_directory(d):
 files=os.listdir(d)
 if not files: return 0
 cnt,total=0,len(files)
 for cnt,f in enumerate(files): os.unlink(d+'/'+f)
 return cnt

def check_temp(d):
 if os.path.isdir(d): print('Deleted %d files in %s' % (clean_directory(d),d))
 else: os.mkdir(d)

def scan_directory(d):
 """Returns list of all files with path in a directory recursively."""
 if not d.endswith(os.sep): d+=os.sep
 rl=[]
 try: files=os.listdir(d)
 except: return []
 for fn in files:
  rl.append(d + fn)
  if os.path.isdir(d + fn): rl+=scan_directory(d + fn)
 return sorted(rl)

check_temp(tDir)
photoList=list(filter(lambda x : x[-4:].lower()=='.jpg',scan_directory(startDir)))
img = PIL.Image.open(photoList[0])
xc,yc=img.size[0]/2,img.size[1]/2 # center of circle
rad=min(img.size)/2-min([dvdx,dvdy])/2 # circle radius
ely=(float(img.size[0])/float(img.size[1]))*0.8 # elyptic factor
wg = 2*math.pi/len(photoList)

txt='Photos: %d, \n' % len(photoList)
txt+='Source resolution: %d x %d, \n' % (img.size[0],img.size[1])
txt+='Target resolution: %d x %d, \n' % (dvdx,dvdy)
txt+='Real length: %d seconds, \n' % (len(photoList)/framerate)
txt+='Circle: r = %d, M = %d / %d, ely = %2.2f, v = %2.3f, wink = %2.2f, \n' % (rad,xc,yc,ely,wg,wink)
txt+='Temp dir: %s,\n' % tDir
print(txt)

for cnt,f in enumerate(photoList):
 xi,yi=int(rad*math.sin(wink)*ely)+xc,int(rad*math.cos(wink))+yc
 wink-=wg
 box=int(xi-dvdx/2),int(yi-dvdy/2),int(xi+dvdx/2),int(yi+dvdy/2)
 img = Image.open(f)
 try: img.load()
 except: 
    print('Broken: %s' % f)
    continue
 img=img.crop(box).resize((dvdx,dvdy))
 ofn = '%s/%s' % (tDir, os.path.basename(f))
 img.save(ofn)
 p = os.path.basename(f)
 zeit2 = '%s-%s-%s %s:%s' % (p[0:4], p[4:6], p[6:8], p[9:11], p[11:13])
 cmd = '/home/nyk/Florologium/date_to_image.py', ofn, zeit2
 subprocess.call(cmd)


cmd = 'ffmpeg', '-y', '-hide_banner', '-loglevel', 'panic', '-framerate', framerate, '-pattern_type', 'glob', '-i', '%s/*.jpg' % tDir, '-c:v', 'libx264', '-strict', '-2', '-pix_fmt', 'yuv420p', '-f', 'mp4', mfn
print(cmd)
subprocess.call(cmd)
