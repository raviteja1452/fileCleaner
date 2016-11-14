import ConfigParser
import os, sys, time
from stat import * # ST_SIZE etc

def folderList(path,level,days):
	if os.path.isdir(path) == True:
		l =  os.listdir(path)
		path = path + '/'
		for i in l:
			if os.path.isfile(path+i) == True :
				print level,'File: ',i
				st = os.stat(path+i)
				ti = time.time() - st[ST_ATIME]
				print ti
				print days*60
				if(ti > days*60):
					print 'file to be removed'
			elif os.path.isdir(path+i) == True :
				print level,'Directory: ',i
				folderList(path+i,level+'---',days)
			else:
				print level,'Unknown: ',i


if __name__ == '__main__':
	config = ConfigParser.ConfigParser()
	config.read('fileCleaner.ini')
	print config.sections()
	folderName =  config.get('main','foldername')
	days = config.get('main','daysback')
	folderList(folderName,'---',days)
