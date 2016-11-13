import ConfigParser
import os,sys

config = ConfigParser.ConfigParser
config.read('fileClear.ini')
print config.sections