# Scrape YouTube Channel Videos URL
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

scrape-youtube-channel-videos-url.py is used to grab the video links from a YouTube Channel.

How to use it:
If you want to get all the video links from CBC channel, so just run the command like following:

	python3 scrape-youtube-channel-videos-url.py -b firefox -u "https://www.youtube.com/@CBC/videos"
	python3 scrape-youtube-channel-videos-url.py -b edge -u "https://www.youtube.com/@CBC/videos"
	python3 scrape-youtube-channel-videos-url.py -b chrome -u "https://www.youtube.com/@CBC/videos"
	
Example result CBCtv-202001011120.list was uploaded.

This can be run in Windows or Linux. but don't use the 'root' to run the script in Linux, because seems in Linux you can't use 'root' account to open a browser.

Test results:

	OS	  |	Window10 + python 3.11.2 + selenium 4.8.2 + webdriver-manager 4.0.1	|	    Linux + python 3.9.2 + selenium 4.20.0 + webdriver-manager 4.0.1
	Python3   |	passed	Firefox 125.0.2 (64-bit)                                        |	    passed  Firefox 125.0.3 (64-bit) 
	Python3   |     passeed Edge 124.0.2478.80 (64-bit)                                     |           passed  Edge 124.0.2478.97 (64-bit)
	Python3   | 	passed	Chrome 124.0.6367.202 (64-bit)	                                |	    passed  Chrome 124.0.6367.201 (64-bit)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


If you want to download all the videos you can use youtube-dl:
	
	https://github.com/ytdl-org/youtube-dl

	youtube-dl -a CBCtv-202001011120.list
	
Notice: If you run the Python script in Windows, the end line is CRLF, you need use dos2unix to change it to UNIX format before you start the next steps in Linux.
