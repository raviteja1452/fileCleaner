import ConfigParser
import os, sys, time
import shutil
from stat import * # ST_SIZE etc

def folderList(path,level,days):
	if os.path.isdir(path) == True:
		l =  os.listdir(path)
		path = path + '/'
		for i in l:
			if os.path.isfile(path+i) == True :
				print level,'File: ',i
				st = os.stat(path+i)
				ti = time.time() - st[ST_MTIME]
				if(ti > int(days)*60*60*24):
					try:
						os.remove(path+i)
						print 'file is removed'
					except OSError, e:
						print ("Error: %s - %s." % (e.filename,e.strerror))
			elif os.path.isdir(path+i) == True :
				print level,'Directory: ',i
				folderList(path+i,level+'---',days)
				try:
				    os.rmdir(path + i)
				except OSError as ex:
				    print "directory not empty"
			else:
				print level,'Unknown: ',i


if __name__ == '__main__':
	config = ConfigParser.ConfigParser()
	config.read('fileCleaner.ini')
	folderName =  config.get('main','foldername')
	da = config.get('main','daysback')
	folderList(folderName,'---',da)
