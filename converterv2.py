from PIL import Image
import PIL
import os
import glob
from art import *

Image
# Opening messages
tprint("BRITECODES", "impossible")
print("\033[1;33;40m Hello user welcome to britecodes simple file converter version 2,\n this is based off of Ajeet Vermas code for python picture conversion.\n please ensure the files you wish to convert are within the same folder as the .exe/ .py file.")
# Open image
filein = input("\033[1;32;40m Please type the name of the file (INCLUDING FILE EXT ie. .png .webp ect) and press enter...")

# Choose new file type
newfiletype = input("\033[1;34;40m Please type the desired file format for the file to be converted to (.jpg .png .webp) and press enter...")
image = Image.open(filein)
image.show()

# Convert image to rgb
image = image.convert('RGB')
# Save image
if newfiletype == ".jpg":
    image.save('newimage.jpg', 'jpeg')
elif newfiletype == ".png":
    image.save('newimage.png', 'png')
elif newfiletype == ".webp":
    image.save('newimage.webp', 'webp')
else:
    print("error! invalid file type!")

