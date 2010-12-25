import os
import sys
import getopt

__version__ = ""
__author__ = ""
__data__ = ""

class MetaData(object):
	def __init__(self):
		self.author = None
		self.title = None
		self.data = None
		self.version = None
		self.toc = True
		self.endnotes = True
		self.path = None

def plain_to_hmtl(plain_file):
	pass
	
def join_string(str_list):
	pass

def get_file_content(_file):
	pass
	
def usage():
	pass
	
	
# ///-----Comandline parsing.


if __name__ == "__main__":
	try:
		opts, args = getopt.gnu_getopt(sys.argv[1:], "hfcto", ["help", "file=", "css=","toc","open="])
	except getopt.GetoptError, err:
		print str(err) 
		usage()
		sys.exit(2)
	
	for opt, arg in opts:
		pass
		
		 
		