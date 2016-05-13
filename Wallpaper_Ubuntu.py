#!python3
from bs4 import BeautifulSoup
import urllib.request
import urllib
import os
import re

#Dont forget to replace the [user_name] with the username.

# Opens the BingWallpaper website
with urllib.request.urlopen("http://bingwallpaper.com") as url:
	webpage = url.read()
	
# Stores it in the soup format
soup = BeautifulSoup(webpage,'lxml')

# Gets the first div with the class panel the 
# (first div always contains the latest wallpaper)
div = soup.findAll('div',attrs={"class":"panel"})[0]

# Gets the img tag inside the div tag (this contains the url of the image)
img = div.contents[0].contents[0]


# This gets the image url and stores it in link
link = img.get('src')

# Converts the soup object to string
link = str(link)

# Gets the url of the higher resolution image!
link = link.replace("1366x768","1920x1080")

# Saves image in the local folder
urllib.request.urlretrieve(link,"/home/[user_name]/Pictures/Wallpapers/download.jpg")

# Change the Wallpaper to the newly downloaded image.
os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:/home/[user_name]/Pictures/Wallpapers/download.jpg")
