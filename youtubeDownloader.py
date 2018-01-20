# Developer By : NIRANJAN KUMAR G S 
# From : INDIA
# Email : niranjan4@outlook.in
# Updated date : 20/Jan/2018

import urllib
from bs4 import BeautifulSoup
from pytube import YouTube
import sys


def Youtube(url):
	if "playlist" in url:
		uuu = urllib.urlopen(url).read()
		soup = BeautifulSoup(uuu, 'html.parser')
		a = soup.find_all("td", class_="pl-video-title")
		for i in a:
			links = i.find('a').get('href')
			print 'links',links
			yt = YouTube("https://www.youtube.com" + links)
			yt.streams.first().download()
			continue
		print('complete')
	elif 'watch' in url:
		print url
		yt = YouTube(url)
		yt.streams.first().download()
	else:
		print('url wrong')
a = sys.argv[-1]
Youtube(a)
