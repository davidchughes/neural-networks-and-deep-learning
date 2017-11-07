import time  # delete
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps
from PIL import ImageFilter
#from PIL import ImageEnhance
#from PIL import ImageMath

import random
import numpy as np
import hard_alphabet

bgColor = 255,255,255
textColor = 30,30,30    # gray text is allows the bg to have stronger signal than the data

def jitter(strength):
  return (random.random() - 0.5) * strength

def draw_text(text, text_value, background = 0):  #text should be 3 chars 'garbage char'+'important char'+'garbage char', text val 0-9, bg 0-6
  # As any bad function, this returns just a bit more than what you may have been expecting.
  # Since I'm drawing an image and will want 4 other enhancemnets of that image, just go ahead and make them and return them as an array of all 5 in the same format as 1 data point of the the mnist data
  rotation = jitter(5)    # rotation 0deg +/- 2.5deg 

  font = ImageFont.truetype("/Library/Fonts/Andale Mono.ttf",250)  #Courier New.ttf",250)#Andale Mono.ttf",250) #Arial.ttf",250)  #change for PC

  if background == 0 :
    img=Image.new("RGB", (280,280),bgColor)
  else:
    if background == 1 :
      img = Image.open("../data/bg1.png")
      scale_size = 28               # scale_size is the size the max text height should be in pixels in the image
    elif background == 2 :
      img = Image.open("../data/bg2.png")
      scale_size = 180
    elif background == 3 :
      img = Image.open("../data/bg3.png")
      scale_size = 140
    elif background == 4 :
      img = Image.open("../data/bg4.png")
      scale_size = 100
    elif background == 5 :
      img = Image.open("../data/bg5.png")
      scale_size = 140
    elif background == 6 :
      img = Image.open("../data/bg6.png")
      scale_size = 80
    x = random.randint(0,img.size[0] - scale_size)
    y = random.randint(0,img.size[1] - scale_size)
    img = img.crop((x,y,x+scale_size,y+scale_size))
    #grow to 280x280 so text placement can be accurately placed with .1 subpixel resolution
    img = img.resize((280,280), PIL.Image.BICUBIC) # Bicubic to get as much artifact as possible - make it hard
  draw = ImageDraw.Draw(img)
  draw.text((-90 + jitter(4), 0 + jitter(4)),text,textColor,font=font)
  draw = ImageDraw.Draw(img)
  img = img.rotate(rotation, PIL.Image.BILINEAR)#PIL.Image.BICUBIC)
  img = img.crop((30 + jitter(30),30 + jitter(30),250 + jitter(30),250 + jitter(30))) # stretch a bit every way - I regret using jitter() as +/- but if I switch to gausian its easy
  img = img.resize((28,28), PIL.Image.BILINEAR)#PIL.Image.LANCZOS)  #squish back to 28x28.  Bilinear is most like native resolution as a scanner would give you
  img = img.convert('L')
  img_e1 = img.filter(ImageFilter.UnsharpMask(radius=1.8, percent=250, threshold=0)) #Similar to what looks like a scanner

  img_e2 = img.filter(ImageFilter.UnsharpMask(radius=3, percent=250, threshold=0))
  
  img_e3 = img.filter(ImageFilter.GaussianBlur(radius=(1.4)))
  img_e3 = img_e3.filter(ImageFilter.UnsharpMask(radius=2.8, percent=150, threshold=0))
  
  img_e4 = img_e3.filter(ImageFilter.UnsharpMask(radius=6, percent=100, threshold=0))

  img = ImageOps.invert(img)
  img = img.convert('F')
  arr = np.array(img)/255.0
  arr = arr.flatten()             #e0 = no enhancement

  #print arr
  #img.save(str(text_value)+".png")

  img_e1 = ImageOps.invert(img_e1)
  img_e1 = img_e1.convert('F')
  arr_e1 = np.array(img_e1)/255.0
  arr_e1 = arr_e1.flatten()

  img_e2 = ImageOps.invert(img_e2)
  img_e2 = img_e2.convert('F')
  arr_e2 = np.array(img_e2)/255.0
  arr_e2 = arr_e2.flatten()

  img_e3 = ImageOps.invert(img_e3)
  img_e3 = img_e3.convert('F')
  arr_e3 = np.array(img_e3)/255.0
  arr_e3 = arr_e3.flatten()

  img_e4 = ImageOps.invert(img_e4)  #Just one more - haha.  Seriously fix this insane repetition
  img_e4 = img_e4.convert('F')
  arr_e4 = np.array(img_e4)/255.0
  arr_e4 = arr_e4.flatten() 

  #this crazy return type deserves to be objects or flattened or some how split apart in a reasonable way
  return ((arr, text_value), (arr_e1, text_value), (arr_e2, text_value), (arr_e3, text_value), (arr_e4, text_value))   #preserve conpatibility with mnist data setup
  
def draw_rand_text(background = 3, char_set = 1):

  pre = hard_alphabet.num_to_chars(random.randint(0,9),char_set)
  value = random.randint(0,9)
  x = hard_alphabet.num_to_chars(value,char_set)
  post = hard_alphabet.num_to_chars(random.randint(0,9),char_set)
  text = pre + x + post

  return draw_text(text, value, background)



