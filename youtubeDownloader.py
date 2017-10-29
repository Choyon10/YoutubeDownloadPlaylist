import urllib.request
from bs4 import BeautifulSoup
from pytube import YouTube
import os


def Youtube(url, file):
	newpath = r'{}'.format(file)
	# try:
	if "playlist" in url:
		uuu = urllib.request.urlopen(url).read()
		soup = BeautifulSoup(uuu, 'html.parser')
		a = soup.find_all("td", class_="pl-video-title")
		# fil=soup.find("h1", class_="pl-header-title").text
		for i in a:
			links = i.find('a').get('href')
			yt = YouTube("https://www.youtube.com" + links)
			# video= yt.get_videos()
			print(yt.filename)
			try:
				video = yt.get('mp4', '720p')
			except:
				continue
			file = os.path.exists(newpath)
			if not file:
				os.makedirs(newpath)
			ff=r'C:\{}\{}.mp4'.format(file,yt.filename)
			if os.path.exists(ff):
				continue
			video.download(newpath)
		print('complete')
	elif 'watch' in url:
		yt = YouTube(url)
		yt.get_videos()
		print(yt.filename)
		video = yt.get('mp4', '720p')

		file = os.path.exists(newpath)
		if not file:
			os.makedirs(newpath)

		video.download(newpath)
	else:
		print('url wrong')
	# except OSError:
	# 	print('file already exist '+yt.filename)
b=input('enter folder name : ')
a= input('enter Youtube url-link  : ')
Youtube('{}'.format(a),b)
