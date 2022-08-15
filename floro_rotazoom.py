#!/usr/bin/python
# Rotating zoom timelapse
# 2010-06-21 by Nick Fankhauser
# 2014-03-24: simplified
import sys,os,time,Image,math,progressbar,katzlib,numpy,subprocess

framerate=25
#wink = math.pi
#wink = 0
wink = math.pi / 2
anzahl_zooms = 4
minzoom=0.8 # minimal zoom factor
dvdx,dvdy = 640, 480 # target resolution (DVD: 720,576)
if len(sys.argv)>2: lores = int(sys.argv[2])
else: lores = 0
if lores: dvdx,dvdy = 320, 240
do_rotamirr=False
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

def create_zoomlist(zoomsteps,minzoom,maxzoom):
 sinlist=map(math.sin,numpy.arange(0,math.pi,math.pi/zoomsteps).tolist()) 
 return map(lambda x : x/(float(sum(sinlist)-0)/(maxzoom-minzoom)),sinlist)

def check_temp(d):
 if os.path.isdir(d): print 'Deleted %d files in %s' % (clean_directory(d),d)
 else: os.mkdir(d)

def rotamirr(img):
 img_rot=img.rotate(-mirr_angle,expand=1)
 img_crop=img_rot.crop((0,0,img_rot.size[0],int(img_rot.size[1]/cutfakt)))
 img_flip = img_crop.transpose(Image.FLIP_TOP_BOTTOM)
 img_new=Image.new('RGB',(img_crop.size[0],img_crop.size[1]*2))
 img_new.paste(img_crop,(0,0))
 img_new.paste(img_flip,(0,img_crop.size[1]))
 img_unrot=img_new.rotate(mirr_angle)
 for y in range(0,img_unrot.size[1]):
  if img_unrot.getpixel((img_unrot.size[0]/2,y))!=(0,0,0): break
 for x in range(0,img_unrot.size[0]):
  if img_unrot.getpixel((x,y))!=(0,0,0): break
 img_unrot_crop=img_unrot.crop((x,y,x+img.size[0],y+img.size[1]))
 return img_unrot_crop

check_temp(tDir)
photoList=filter(lambda x : x[-4:].lower()=='.jpg',katzlib.scan_directory(startDir,False))
zf=minzoom
zommdirection=1
img=Image.open(photoList[0])
maxzoom=img.size[0]/2.0/dvdx
xc,yc=img.size[0]/2,img.size[1]/2 # center of circle
rad=min(img.size)/2-min([dvdx*maxzoom,dvdy*maxzoom])/2 # circle radius
ely=(float(img.size[0])/float(img.size[1]))*0.95 # elyptic factor
zoomlist=create_zoomlist(len(photoList)/anzahl_zooms,minzoom,maxzoom)
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

idx=0
for cnt,f in enumerate(photoList):
 xi,yi=int(rad*math.sin(wink)*ely)+xc,int(rad*math.cos(wink))+yc
 wink-=wg
 box=int(xi-dvdx/2*zf),int(yi-dvdy/2*zf),int(xi+dvdx/2*zf),int(yi+dvdy/2*zf)
 img = Image.open(f)
 if do_rotamirr: img = rotamirr(img)
 img=img.crop(box).resize((dvdx,dvdy))
 #if lores: img = img.resize((640,480), Image.ANTIALIAS)
 ofn = '%s/%s' % (tDir, os.path.basename(f))
 img.save(ofn)
 if lores: subprocess.call(['hqx','-s','2',ofn,ofn])
 idx+=1
 zf+=zoomlist[idx]*zommdirection
 if idx==len(zoomlist)-1:
  zommdirection*=-1
  idx=0

