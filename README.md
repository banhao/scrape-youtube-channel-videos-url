scrape-youtube-channel-videos-url.py is used to grab the video links from a YouTube Channel.

How to use it:
If you want to get all the video links from CBC channel, so just run the command like following:

	python3 scrape-youtube-channel-videos-url.py https://www.youtube.com/user/CBCtv/videos
	
Example result CBCtv-202001011120.list was uploaded.

This can be run in Windows or Linux. but don't use the 'root' to run the script in Linux, because seems in Linux you can't use 'root' account to open a browser.

Please install the "selenium" first.
	
	https://pypi.org/project/selenium/

And you also need to download the browser drivers
	
	https://selenium-python.readthedocs.io/installation.html#drivers

Test results:

	OS			|	Window10	|	Linux
	Python3 + FireFox	|	passed		|	passed
	Python3 + Chrome	|	passed		|	haven't installed the chrome 
------------------------------------------------------------------------

I didn't test in IE and Edge, because I rarely use that 2 browers.

If you want to download all the videos you can use youtube-dl:
	
	https://github.com/ytdl-org/youtube-dl

	youtube-dl -a CBCtv-202001011120.list
	
Notice: If you run the Python script in Windows, the end line is CRLF, you need use dos2unix to change it to UNIX format before you start the next steps in Linux.
