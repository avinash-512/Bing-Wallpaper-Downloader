#! /bin/bash
U=$USER
su
read USE
sudo apt-get install python3
sudo pip install bs4
sudo pip install crontab-python
sudo pip install urllib
sudo mkdir /home/$U/Bing_Wallpaper2.0
sudo cp $PWD/Wallpaper_Ubuntu.py /home/$U/Bing_Wallpaper2.0/ -r
SCRIPT_PATH=/home/$U/Scripts/Wallpaper_Ubuntu.py
sudo /usr/bin/python3 $SCRIPT_PATH


