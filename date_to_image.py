#!/usr/bin/python3
import PIL.Image,os,sys,time

def load_font(fontSize):
 """Load the arial TTF font from the default location for gentoo and debian linux"""
 import PIL.ImageFont
 f1 = '/usr/share/fonts/corefonts/arialbd.ttf' 
 f2 = '/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf'
 if os.path.isfile(f1): font=PIL.ImageFont.truetype(f1,fontSize)
 if os.path.isfile(f2): font=PIL.ImageFont.truetype(f2,fontSize)
 return font

def draw_date(img,txs):
 """Write date and time in the image"""
 import PIL.ImageDraw
 fontSize=int(img.size[1]/20)
 draw = PIL.ImageDraw.Draw(img) # new draw instance 
 arial=load_font(fontSize)
 draw.text((10, 10), txs, fill='white', font=arial)
 return img

fn = sys.argv[1]
txs = sys.argv[2]
i = PIL.Image.open(fn)
i2 = draw_date(i,txs)
i2.save(fn)
