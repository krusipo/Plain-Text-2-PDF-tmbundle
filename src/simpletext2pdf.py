import os
import sys
import getopt
import os.path

__version__ = "0.3"
__author__ = "Jonas Odencrants"
__date__ = ""

class MetaData(object):
	def __init__(self, plain_file):
		
		for key, value in self.file_vars(plain_file).iteritems():
			self.__dict__[key] = value

		
	def file_vars(self, plain_file):
		
		local_vars = open(plain_file, 'r')
		simple_vars = local_vars.readline()
		file_meta = {}
		file_meta["toc"] = True
		file_meta["author"] = ''
		file_meta["version"] = ''
		file_meta["title"] = 'README'
		file_meta["date"] = self.getDate()
		file_meta["toc"] = True
		try:
			simple_vars.index('<!--Simple')
			simple_vars = simple_vars.replace('<!--Simple ', '').replace(' -->', '')
			temp = [s for s in simple_vars.split(';') if s]
			for item in temp:
			    key,value = item.split(':')
			    file_meta[key] = value
		except ValueError:
			print("Meta must be on first line and like this <!--Simple author:The Author; -->")
		
		finally:
			file_meta["dir"] = os.path.dirname(plain_file)
			file_meta["file_name"] = os.path.basename(plain_file)
			
			
		return file_meta
		
	def getDate(self):
		from datetime import date
		return date.today()
		 
class Template(object):
	def __init__(self):
		self._head = '<!DOCTYPE HTML><html><head><title>Simple Syntax Document</title>\
						<meta charset="utf-8" /><style type="text/css"></style></head><body>'
		self._end = '</body></html>'
		
		self.meta = None
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
	plain_type = {".md" : markdown,
				".MD" : markdown,
	}
	
	return plain_type[os.path.splitext(plain_file)](plain_file)

def markdown(plain_file):
	import markdown2
	extras=["code-color","footnotes"]
	return markdown2.markdown_path(plain_file, extras)
	
def join_string(str_list):
	pass

def get_file_content(_file):
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
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt in ("-f", "--file"):
			# File object to get plain-text syntax from.
				m = MetaData(arg)
				print(m.toc)
		elif opt in ("-c", "--css"):
			# Use specified css file.
			pass
		else:
			assert False, "unhandled option"
	
	
		
		 
		