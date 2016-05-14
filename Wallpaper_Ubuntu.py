#!python3
from bs4 import BeautifulSoup
import urllib.request
import urllib
import os
import re
from crontab import CronTab

#Stores the current user_name in the user_name variable
user_name = os.popen('echo "$USER"').read().rstrip()



def download_image(link,picture_name):
	#Stores the Download path in the variable: download_path
	download_path = "/home/"+user_name+"/Pictures/Wallpapers/"+picture_name

	# Saves image in the local folder
	urllib.request.urlretrieve(link,download_path)

	
	#Stores the command to change the wallpaper
	change_command = "/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:/home/"+user_name+"/Pictures/Wallpapers/"+picture_name

	# Change the Wallpaper to the newly downloaded image.
	os.system(change_command)
	


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


	# This gets the image url and stores it in link\
	link = img.get('src')

	# Converts the soup object to string
	link = str(link)

	# Gets the url of the higher resolution image!
	link = link.replace("1366x768","1920x1080")

	#Stores the name of the picture in the picture_name variable
	picture_name = link.replace("https://www.bing.com/az/hprichbg/rb/","")
	picture_name = picture_name.split("_")[0]+".jpg"
	
	return link,picture_name
	
	
	
def find_comment(users_cron,com):
	p = 1
	i = 0
	for job in users_cron:
		if job.comment == com:
			index = i
			p = 0
		i = i+1
	if p:
		return 0,0
	else:
		return 1,index
		
		
		
def modify_schedule(a):
	users_cron    = CronTab(user=user_name)
	cmd = "/usr/bin/python3 /home/"+user_name+"/Scripts/Wallpaper_Ubuntu.py"
	if a:
		flag,index = find_comment(users_cron,"13:00")
		if not flag:
			job = users_cron.new(command=cmd,comment="13:00")
			job.hour.on(13)
			job.minute.also.on(0)
		else:
			job = users_cron[index]
			job.enable()
		users_cron.write()
		
		flag,index = find_comment(users_cron,"every_hour")
		if not flag:
			job = users_cron.new(command=cmd,comment="every_hour")
			job.minute.also.on(0)
		else:
			job = users_cron[index]
			job.enable(False)
		users_cron.write()	
	else:
		flag,index = find_comment(users_cron,"every_hour")
		if not flag:
			job = users_cron.new(command=cmd,comment="every_hour")
			job.minute.also.on(0)
		else:
			job = users_cron[index]
			job.enable()
		users_cron.write()
		
		
	
def move_pictures(downloaded,picture_name):
	for img in downloaded:
		if (not img == picture_name) and (not img == "Bing_Wallpapers"):
			source = "/home/"+user_name+"/Pictures/Wallpapers/"+img
			dest = "/home/"+user_name+"/Pictures/Wallpapers/Bing_Wallpapers/"+img
			cmd = "mv -f "+source+" "+dest	
			os.system(cmd)
			
			
		
def create_folders():
	folders = os.popen("ls /home/"+user_name+"/Pictures/").read().split("\n")
	folders.remove('')
	p = 1
	for files in folders:
		if files == "Wallpapers":
			p = 0
	if p:
		os.system("mkdir /home/"+user_name+"/Pictures/Wallpapers")
		os.system("mkdir /home/"+user_name+"/Pictures/Wallpapers/Bing_Wallpapers")
	folders = os.popen("ls /home/"+user_name+"/Pictures/Wallpapers").read().split("\n")
	folders.remove('')
	p = 1
	for files in folders:
		if files == "Bing_Wallpapers":
			p = 0
	if p:
		os.system("mkdir /home/"+user_name+"/Pictures/Wallpapers/Bing_Wallpapers")

def is_aldready_downloaded(picture_name):
	downloaded = os.popen("ls /home/"+user_name+"/Pictures/Wallpapers").read().split("\n")
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
	create_folders()
	flag,downloaded = is_aldready_downloaded(picture_name)
	if not flag:
		download_image(link,picture_name)
		modify_schedule(1)
		move_pictures(downloaded,picture_name)
	else:
		modify_schedule(0)
		move_pictures(downloaded,picture_name)
	

