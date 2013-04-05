#!/usr/bin/python

from subprocess import Popen, PIPE
from shlex import split

files = Popen(split('find . -name "*.MP4"'), stdout=PIPE).communicate()[0].strip().split('\n')
#print files

from os import remove
from os.path import dirname, basename, exists, getsize

for file in files:
	#print dirname(file)+' / '+basename(file)
	newname = basename(file)[:-4]+'.avi'
	newpath = dirname(file)+'/'+newname
	# remove empty file
	if (exists(newpath) and (getsize(newpath) == 0)):
		print 'Empty file: '+newpath+'. Removing...'
		#remove(newpath)
	# don't overwrite existing file
	if (newname != basename(file)) and (not exists(newpath)):
		cmd = 'ffmpeg -i "'+file+'" -deinterlace -sameq -acodec copy "'+newpath+'"'
		print cmd
		Popen(split(cmd)).wait()
	else:
		print 'File exists: '+newpath+'. Aborting.'
