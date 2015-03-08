import Image
from PIL import ImageFont
from PIL import PngImagePlugin
from PIL import ImageDraw 
import os

def makeinvit(firstname, familyname):
	img = Image.open("/var/www/pi/piday/subscription/invitation.png")
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("/var/www/pi/piday/subscription/OpenSans.ttf", 65)

	a={}
	coordinate={}
	print "bbbbbbbbbbbbbbb"
	img = Image.open("/var/www/pi/piday/subscription/invitation.jpg")		
	draw = ImageDraw.Draw(img)

	a["familyname"]=familyname
	a["firstname"]=firstname

	w, h = draw.textsize("Whatever",font)

	h=h/2

	print "bbbbbbbbbbbbbbb"

	coordinate["firstname"]=(330,1121-h)
	coordinate["familyname"]=(330,1251-h)

	for i in a:
		draw.text(coordinate[i],a[i],(0,0,0),font=font)


	img.save("/var/www/pi/piday/subscription/result/"+a["firstname"]+a["familyname"]+".png")

