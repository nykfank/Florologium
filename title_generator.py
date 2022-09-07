#!/usr/bin/python3
# Add title to the first few images of a movie
import PIL.Image,PIL.ImageDraw,PIL.ImageFont,os,sys,math
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
font_path='/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
indir=sys.argv[1].rstrip('/') # input directory containing only movie frames
numframes = int(sys.argv[2]) # number of images to add the title to
text = sys.argv[3], sys.argv[4], sys.argv[5]

def add_title(f,n):
 path='%s/%s' % (indir,f) # full path to an PIL.Image
 img=PIL.Image.open(path) # open the PIL.Image
 s=img.size # size of the PIL.Image
 
 fimg=PIL.Image.new('L',s,0) # mask: Gray scale PIL.Image of same size and black background
 fimg_draw = PIL.ImageDraw.Draw(fimg) # used to draw text on it
 font_size=s[0]/15 # font size proportional to PIL.Image size
 addy=0 # vertical shift of text rows
 alpha=255*math.sin(float(n)/float(numframes)*math.pi) # transparency factor
 for nt,t in enumerate(text): # for all rows of text
  font=PIL.ImageFont.truetype(font_path, int(font_size)) # create the font
  ts=fimg_draw.textsize(t,font=font) # size of text bounding box using this font
  pos=(s[0]-ts[0])/2, s[1]/2-ts[1]*3/2 + addy # position of text
  fimg_draw.text(pos,t,fill=int(alpha),font=font) # write text to mask
  addy+=ts[1] # add vertical size of bounding box to shift
  if nt: font_size/=2 # decrease font size
 solid=PIL.Image.new('RGB',s,(200,200,255)) # solid PIL.Image for text color
 cimg=PIL.Image.composite(solid,img,fimg) # merge the solid to the PIL.Image using the mask
 cimg.save(path) # and overwrite the PIL.Image on disk

files=sorted(os.listdir(indir)) # all files in the input directory
for n,f in enumerate(files[:numframes]): # look the first selected number of PIL.Images
 add_title(f,n) # add the title with transparency depending on the index
 
