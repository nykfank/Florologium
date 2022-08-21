#!/usr/bin/python
# Rotating zoom timelapse
# 2010-06-21 by Nick Fankhauser
# 2014-03-24: simplified
import sys,os,time,Image,math,progressbar,katzlib,numpy,subprocess

framerate=20
#wink = math.pi
#wink = 0
wink = math.pi / 2
dvdx,dvdy = 640, 480 # target resolution (DVD: 720,576)
mirr_angle,cutfakt=30,1.53 # try1

starttime=time.time()
default_widgets=[progressbar.Percentage(), ' ', progressbar.Bar(), progressbar.ETA()]
startDir=os.path.abspath(sys.argv[1]).rstrip('/')+'/'
tDir ='%s_rota' % startDir.rstrip('/')

def clean_directory(d):
 pbar = progressbar.ProgressBar(widgets=['Cleaning: '] + default_widgets).start()
 files=os.listdir(d)
 if not files: return 0
 cnt,total=0,len(files)
 for cnt,f in enumerate(files): 
  os.unlink(d+'/'+f)
  pbar.update(float(cnt)/float(total)*100)
 pbar.finish()
 return cnt

def check_temp(d):
 if os.path.isdir(d): print 'Deleted %d files in %s' % (clean_directory(d),d)
 else: os.mkdir(d)

check_temp(tDir)
photoList=filter(lambda x : x[-4:].lower()=='.jpg',katzlib.scan_directory(startDir,False))
img=Image.open(photoList[0])
maxzoom=img.size[0]/2.0/dvdx
xc,yc=img.size[0]/2,img.size[1]/2 # center of circle
rad=min(img.size)/2-min([dvdx*maxzoom,dvdy*maxzoom])/2 # circle radius
ely=(float(img.size[0])/float(img.size[1]))*0.95 # elyptic factor
wg = 2*math.pi/len(photoList)

txt='Photos: %d, \n' % len(photoList)
txt+='Source resolution: %d x %d, \n' % (img.size[0],img.size[1])
txt+='Target resolution: %d x %d, \n' % (dvdx,dvdy)
txt+='Real length: %d seconds, \n' % (len(photoList)/framerate)
txt+='Circle: r = %d, M = %d / %d, ely = %2.2f, v = %2.3f, wink = %2.2f, \n' % (rad,xc,yc,ely,wg,wink)
txt+='MaxZoom = %2.2f, MinZoom = %2.2f, \n' % (maxzoom,minzoom)
txt+='ZoomSteps = %d, sum(zoomlist) = %2.2f, \n' % (len(zoomlist),sum(zoomlist))
if do_rotamirr: txt+='Mirror: %s, Mirror Angle = %d, cutfakt = %2.2f.\n' % (do_rotamirr,mirr_angle,cutfakt)
txt+='Temp dir: %s,\n' % tDir
print txt

for cnt,f in enumerate(photoList):
 xi,yi=int(rad*math.sin(wink)*ely)+xc,int(rad*math.cos(wink))+yc
 wink-=wg
 box=int(xi-dvdx/2),int(yi-dvdy/2),int(xi+dvdx/2),int(yi+dvdy/2)
 img = Image.open(f)
 img=img.crop(box).resize((dvdx,dvdy))
 ofn = '%s/%s' % (tDir, os.path.basename(f))
 img.save(ofn)

