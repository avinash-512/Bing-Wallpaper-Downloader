#! /bin/bash
U=$USER
sudo apt-get install python3
sudo apt-get install python-setuptools python-dev build-essential
sudo apt install pip
sudo pip install bs4
sudo pip install urllib
sudo mkdir /home/$U/Bing_Wallpaper2.0
sudo cp $PWD/Wallpaper_Ubuntu.py /home/$U/Bing_Wallpaper2.0/
SCRIPT_PATH=/home/$U/Bing_Wallpaper2.0/Wallpaper_Ubuntu.py
sudo /usr/bin/python3 $SCRIPT_PATH
mkdir /home/$U/Pictures/Bing-Wallpapers
crontab -l > mycron
echo "@hourly /usr/bin/python3 /home/$U/Bing_Wallpaper2.0/Wallpaper_Ubuntu.py" >> mycron
crontab mycron
rm mycron
crontab -l > mycron
echo "@reboot /usr/bin/python3 /home/$U/Bing_Wallpaper2.0/Wallpaper_Ubuntu.py" >> mycron
crontab mycron
rm mycron



