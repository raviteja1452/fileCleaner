import ConfigParser
import os,sys

config = ConfigParser.ConfigParser()

config.read('fileCleaner.ini')
print config.sections()
print config.get('main','foldername')
print config.get('main','daysback')
