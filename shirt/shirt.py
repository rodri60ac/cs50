import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few arguments")
if len(sys.argv) > 3:
    sys.exit("Too many arguments")
if (not os.path.splitext(sys.argv[1])[1] in [".jpg",".jpeg",".png"]) and (not os.path.splitext(sys.argv[2])[1] in [".jpg",".jpeg",".png"]):
    sys.exit("Not an image")
if os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
    sys.exit("Different Formats")

try:
    portrait = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File Not Found")

shirt = Image.open("shirt.png")
size = shirt.size

muppet = ImageOps.fit(portrait,size)

muppet.paste(shirt,shirt)

muppet.save(sys.argv[2])