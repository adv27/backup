#!/usr/bin/python
import os
import requests
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

AUTHOR = "Tong Vuu"
VERSION = "1.0"

key = ['U', 'W', 'J', 'H', 'D', 'G', 'M', 'A', 'Y', 'I', 'X', 'N', 'R', 'L', 'B', 'P', 'K']
val = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'c', 'u', 'f', 'r', '1', '1', '2']
keymap = dict(zip(key, val))

BTR_LIMIT = "320kbps_MP3"
BTR_FILTER = "/320/"

def decode_key(webkey):
	out = ""
	for k in webkey:
		if k == '-':
			out = out + "-"
		elif k not in key:
			out = out + k
		else:
			out = out + keymap[k]
	return out

def get_page(url):
	response = requests.get(url)
	return response.content

def search(term):
	searchurl = "http://search.chiasenhac.vn/search.php?s=" + term
	res = get_page(searchurl)
	m = re.search('.a href=\"(.*)\" class=\"musictitle\"', res)
	if m is not None:
		songurl = m.group(1)
		return songurl
	return None

def get_file_name(part3):
	return re.sub("%20"," ",re.sub(BTR_FILTER, "", part3))

def write_file(name, res):
	with open(name, 'wb') as f:
		f.write(res)

def download(songurl):
	downloadurl = re.sub(".html", "_download.html", songurl)
	res = get_page(downloadurl)
	m = re.findall("decode_download_url\((.*), 1\)", res)
	for l in m:
		if l.find(BTR_LIMIT) != -1:
			p = l.split("', '")
			url = re.sub("'ht","ht",p[0]) + decode_key(p[1]) + re.sub("'","",p[2])
			print url
			res = get_page(url)
			write_file(get_file_name(re.sub("'","",p[2])), res)
			return True
	print "Can't find download BTR"
	return False

def download_list(fname): # Dowload based on a list of song url
	with open(fname, "r") as f:
		for line in f:
			download(line)
			print "Downloaded %s" % line

def download_list_name(fname): # Dowload a list of songs name
	with open(fname, "r") as f:
		for sname in f:
			url = search(sname)
			if url:
				download(url)
				print "Downloaded %s" % sname
			else:
				print "Can't find %s" % sname

if __name__ == "__main__":
	while True: # I Love this print
		print "Welcome to CSN Song Downloader v%s by %s" % (VERSION, AUTHOR)
		print "1. Dowload a list of song url"
		print "2. Dowload a list of song name (require search)"
		print "3. Download a song url (Fast)"
		print "4. Download a song name (Fast)"
		print "Press other keys to exit"
		choice = raw_input("What can I help you? > ")
		if choice == "1" or choice == "2":
			fname = raw_input("Input the name of the file > ")
			if choice == 1:
				download_list(fname)
			else:
				download_list_name(fname)
		elif choice == "3" or choice == "4":
			fastname = raw_input("Input a song name or url > ")
			if choice == 3:
				download(fastname)
			else:
				url = search(fastname)
				if url:
					download(url)
		else:
			print "Thanks for using"
			exit()

