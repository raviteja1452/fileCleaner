import ConfigParser
import os,sys

def folderList(path):
	
if __name__ == '__main__':
	config = ConfigParser.ConfigParser()
	config.read('fileCleaner.ini')
	print config.sections()
	folderName =  config.get('main','foldername')

	# Printing the Contents of the folder
	l =  os.listdir(folderName)
	path = folderName+'/'
	print l
	for i in l:
		if os.path.isfile(path+i) == True :
			print i,'is a file'
		elif os.path.isdir(path+i) == True :
			print i,'is a directory'
		else:
			print i,'is a unknown'
