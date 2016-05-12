# BING WALLPAPER DOWNLOADER
This script downloads the bing wallpaper of the day and sets it as your desktop wallpaper.

<h4>To run this in Ubuntu :</h4>
- Copy the script to a folder
- Use crontab to schedule this script to run at a specific time everyday.
- run the following command

> crontab -e

- add this to the crontab file and save.

> xx yy * * * /usr/bin/python3 /home/****(pathname)

replace xx with minutes and yy with hour of the day at which you want to download the wallpaper.

