import os
import sys
import getopt
import os.path

__version__ = "0.3"
__author__ = "Jonas Odencrants"
__date__ = "2010-12-25"

class MetaData(object):
	"""A class with passable meta and settings."""
	def __init__(self, plain_file):
		"""Constructor takes a plain-file.format and inits meta."""
		for key, value in self.__file_vars(plain_file).iteritems():
			self.__dict__[key] = value

	def __file_vars(self, plain_file):
		"""
		Set dictionary for meta object when plain file supports
		local vars syntax.
		return dict toc, author,version,title,date,dir,file_name
		"""
		local_vars = open(plain_file, 'r')
		simple_vars = local_vars.readline()
		local_vars.close()
		file_meta = {}
		file_meta["toc"] = True
		file_meta["author"] = ''
		file_meta["version"] = ''
		file_meta["title"] = 'README'
		file_meta["date"] = self.__getDate()
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
		
	def __getDate(self):
		from datetime import date
		return date.today()
		 
		
class DomTemplate(object):
	
	def __init__(self, meta_obj):
		self._meta = meta_obj
		self.css = None
		self.plain_text = None
		self.html = '<!DOCTYPE HTML><html><head><title>$title</title>\
						<meta charset="utf-8" /><style type="text/css">$css_file</style></head><body>\
						<table id="simple_text_head"><tr><td class="simple_text_title">$title</td>\
						<td class="simple_text_author">$author</td></tr></table>\
						<div id="simple_plain_text">$plain_text</div>\
						<table id="simple_text_foot"><tr><td class="simple_text_date">$date</td>\
						<td class="simple_text_pageno"><pdf:pagenumber></td></tr></table>\
						</body></html>'
		
	def appendTo(tag):
		pass
		
	def toString(self):
		from string import Template
		references = self._meta.__dict__.copy()
		references['css_file'] = self.css
		references['plain_text'] = self.plain_text
		
		html = Template(self.html).substitute(references)
		return html
		
	def toUnicodeString(self):
		pass

# ///-----Global functions.

def plain_to_hmtl(plain_file):
	plain_type = {".md" : markdown,
				".MD" : markdown,
	}
	file_type = os.path.splitext(plain_file)[1]
	return plain_type[file_type](plain_file)

def markdown(plain_file):
	import markdown2
	return markdown2.markdown_path(plain_file, extras=["code-color","footnotes"])

def get_file_content(_file):
	"""Return String - filecontents
	Pre: file is a filepath.
	"""
	data = open(_file, 'r')
	content = data.read()
	data.close()
	return content
	
def usage():
	pass
	
def build(_file):
	meta = MetaData(_file)
	dom = DomTemplate(meta)
	dom.plain_text = plain_to_hmtl(_file).encode( "utf-8" )
	print(dom.toString())
	
if __name__ == "__main__":
	try:
		opts, args = getopt.gnu_getopt(sys.argv[1:], "hf:", ["help", "file="])
	except getopt.GetoptError, err:
		print str(err) 
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt in ("-f", "--file"):
			build(arg)
		else:
			assert False, "unhandled option"