# daily-update.py
#
# Get the latest movie of modeled currents from LiveOcean and decompose it into hourly images
#
# Created 4/24/2022 by scottveirs and ammended by valveirs 5/3/2022


from datetime import datetime
import os
import requests
from PIL import Image

def thumbnails(savedir, imgfile, scalefactor):
   try:
      image = Image.open(imgfile)
      image.thumbnail((image.height//scalefactor, image.width//scalefactor))
      thmfile = savedir + imgfile.split("/")[-1]
      image.save(thmfile)
      # image1 = Image.open(thmfile)
      # image1.show()
   except IOError:
      pass
#################################################
# Get today's date and print it

date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
print(f"filename_{date}")

# Use Requests to download the latest model movie from the LiveOcean site
# Store the mp4 in /data/latest-LO
cwd = os.getcwd()
currentfile = "https://faculty.washington.edu/pmacc/LO/Figs_active_forecast/P1_PS_speed_top.mp4"
print("Current working directory is", cwd)
print("ls is", os.listdir())
r = requests.get(currentfile, allow_redirects=True)
open('{}/data/latest-LO/P1_PS_speed_top.mp4'.format(cwd), 'wb').write(r.content)

# Use ffmpeg to extract frames from each hour as individual image files

os.system('ffmpeg -i {}/data/latest-LO/P1_PS_speed_top.mp4 -vf fps=8 {}/data/latest-LO/img/plot_%04d.png'.format(cwd, cwd))
scalefactor = 3    # scalefactor = 2 give a more 'readable' thumbnail
imgDir = "{}/data/latest-LO/img/".format(cwd)
print(imgDir)
for file in os.listdir(imgDir):
    print(file)
    thumbnails("{}/data/latest-LO/thumbs/".format(cwd), "{}/data/latest-LO/img/".format(cwd) + file, 3)

# Store the output in /data/latest-LO

# Move any older files from /data/latest-LO to /data/archive-LO


