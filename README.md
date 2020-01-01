scrape-youtube-channel-videos-url.py is used to grab the video links from a YouTube Channel.

How to use it:
If you want to get all the video links from CBC channel, so just run the command like following:

	python3 scrape-youtube-channel-videos-url.py https://www.youtube.com/user/CBCtv/videos

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

I didn't tested in IE and Edge, because I rarely use that 2 browers.
