import os
import sys
import getopt

__version__ = ""
__author__ = ""
__data__ = ""

class MetaData(object):
	def __init__(self, atoc = True,):
		self.author = None
		self.title = None
		self.date = None
		self.version = None
		self.toc = atoc
		self.endnotes = True
		self.path = None
		
class Template(object):
	def __init__(self):
		self._head = '<!DOCTYPE HTML><html><head><title>Simple Syntax Document</title>\
						<meta charset="utf-8" /><style type="text/css"></style></head><body>'
		self._end = '</body></html>'
		
		self.meta = MetaData()
		self.simple_text = None
		self.header = None
		self.footer = None
		
		
	def appendTo(tag):
		pass
		
	def toString(self):
		pass
		
	def toUnicodeString(self):
		pass

# ///-----Global functions.

def plain_to_hmtl(plain_file):
	pass
	
def join_string(str_list):
	pass

def get_file_content(_file):
	filetype = {'md' : markdown,
	}
	pass
	
def usage():
	pass
	
	
# ///-----Comandline parsing.


if __name__ == "__main__":
	try:
		opts, args = getopt.gnu_getopt(sys.argv[1:], "hf:c:", ["help", "file=", "css="])
	except getopt.GetoptError, err:
		print str(err) 
		usage()
		sys.exit(2)
	
	for opt, arg in opts:
		pass
		
		 
		