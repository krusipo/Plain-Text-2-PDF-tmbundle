import os
import sys
import getopt
import os.path
import cStringIO

__author__ = "Jonas Odencrants"
__date__ = "2010-12-31"

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
			print("Meta must be on first line and like this \
			<!--Simple author:The Author; -->")
		
		finally:
			file_meta["dir"] = os.path.dirname(plain_file)+'/'
			file_meta["file_name"] = os.path.basename(plain_file)
			
			
		return file_meta
		
	def __getDate(self):
		from datetime import date
		return date.today()
		 
		
class DomTemplate(object):
	"""HTML template to convert to pdf"""
	def __init__(self, meta_obj):
		self._meta = meta_obj
		self.plain_text = None
		basepath = os.path.realpath( __file__ )

		self.css = os.path.split(basepath)[0]+'/default-style.css'
		if "css" in self._meta.__dict__:
			self.css = self._meta.css 
	
		self.html = os.path.split(basepath)[0]+'/default-template.html'
		if "html" in self._meta.__dict__:
			self.html = self._meta.html
			
		
	def toString(self):
		references = self._meta.__dict__.copy()
		references['plain_text'] = self.plain_text
		references['css_file'] = get_file_content(self.css)
		references['simple_toc'] = ''
			
		if self._meta.toc is True:
			references['simple_toc'] = '<pdf:toc />'
		
		from string import Template
		dom = get_file_content(self.html)
		html = Template(dom).substitute(references)
		return html

# ///-----Global functions.

def plain_to_hmtl(plain_file):
	"""Return String - file content parsed as html
	Pre: plain_file is supported plain-file-syntax.
	"""
	plain_type = {".md" : markdown,
				".MD" : markdown,
	}
	file_type = os.path.splitext(plain_file)[1]
	return plain_type[file_type](plain_file)

def markdown(plain_file):
	"""Return plainfile of type markdown as html"""
	import markdown2
	return markdown2.markdown_path(plain_file, extras=["code-color","footnotes", "code-friendly"])

def get_file_content(_file):
	"""Return String - filecontents
	Pre: file is a filepath.
	"""
	data = open(_file, 'r')
	content = data.read()
	data.close()
	return content
	
def createPDF(meta, html):
	"""
	Creates a pdf and saves at project root.
	"""
	import ho.pisa as pisa
	pdfed = pisa.CreatePDF(
        cStringIO.StringIO(html), file(meta.dir + meta.file_name+".pdf", "wb"))

	if pdfed.err:
		print "*** %d ERRORS OCCURED" % pdf.err
	return pdfed
	
def createHTML():
	"""Create a html and saves at project root"""
	pass
	
def join_string(str_list):
	""" Return String - content from items.
	Pre: str_list as list of strings
	"""
	file_string = cStringIO.StringIO()
	for _str in str_list:
		file_string.write(_str)
	return file_string.getvalue()
	
def usage():
	pass
	
	
def build(_file):
	meta = MetaData(_file)
	dom = DomTemplate(meta)
	dom.plain_text = plain_to_hmtl(_file).encode( "utf-8" )
	createPDF(meta,dom.toString())
		
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