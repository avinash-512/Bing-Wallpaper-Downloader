#!python3
from bs4 import BeautifulSoup
import urllib.request
import urllib
import os
import re

#Stores the current user_name in the user_name variable
user_name = os.popen('echo "$USER"').read().rstrip()


def download_image(link,picture_name):
    #Stores the Download path in the variable: download_path
    download_path = "/home/"+user_name+"/Pictures/Bing-Wallpapers/"+picture_name
    # Saves image in the local folder
    urllib.request.urlretrieve(link,download_path)
    #Stores the command to change the wallpaper
    change_command = "/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:"+download_path
    # Change the Wallpaper to the newly downloaded image
    os.system(change_command)
    return	

def get_wallpaper_link():
    # Opens the BingWallpaper website
    with urllib.request.urlopen("http://bingwallpaper.com") as url:
        webpage = url.read()
	# Stores it in the soup format
    soup = BeautifulSoup(webpage,'lxml')
    # Gets the first div with the class panel the
    # (first div always contains the latest wallpaper
    div = soup.findAll('div',attrs={"class":"panel"})[0]
    # Gets the img tag inside the div tag (this contains the url of the image)
    img = div.contents[0].contents[0]
    # This gets the image url and stores it in link
    link = img.get('src')
    # Converts the soup object to string
    link = str(link)
    # Gets the url of the higher resolution image
    link = link.replace("1366x768","1920x1080")
    #Stores the name of the picture in the picture_name variable
    picture_name = link.replace("https://www.bing.com/az/hprichbg/rb/","")
    picture_name = picture_name.split("_")[0]+".jpg"
    return link,picture_name
	

def is_aldready_downloaded(picture_name):
    downloaded = os.popen("ls /home/"+user_name+"/Pictures/Bing-Wallpapers/").read().split("\n")
    downloaded.remove('')
    p = 1
    for img in downloaded:
        if picture_name == img:
            p = 0
    if p:
        return 0,downloaded
    else:
        return 1,downloaded		
			
			
if __name__ == "__main__":
    link,picture_name = get_wallpaper_link()
    flag,downloaded = is_aldready_downloaded(picture_name)
    if not flag:
        download_image(link,picture_name)


	
