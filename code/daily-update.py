# daily-update.py
#
# Get the latest movie of modeled currents from LiveOcean and decompose it into hourly images
#
# Created 4/24/2022 by scottveirs


from datetime import datetime


# Get today's date and print it

date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
print(f"filename_{date}")


# Use Lynx or Scrapy to scrape the latest model movie from the LiveOcean site


# Store the mp4 in /data/latest-LO


# Use ffmpeg to extract frames from each hour as individual image files

ffmpeg -i P1_PS_speed_top.mp4 -vf fps=8 plot_%04d.png

# Store the output in /data/latest-LO

# Move any older files from /data/latest-LO to /data/archive-LO


