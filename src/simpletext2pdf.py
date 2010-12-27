import os
import sys
import getopt
import os.path
import cStringIO

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
	"""HTML template to convert to pdf"""
	def __init__(self, meta_obj):
		self._meta = meta_obj
		self.plain_text = None
		self.css = '\
		/*==========Body=========*/\
		body {\
			font-size: 110%; /* Base font size: 14px */\
			font-family: "Trebuchet MS", Trebuchet, "Lucida Sans Unicode",\
			"Lucida Grande", "Lucida Sans", Arial, sans-serif;\
			color:rgb(51,51,51);\
		}\
		a {\
		color:rgb(65,142,219); \
		}\
		/*==========Page=========*/\
		@page {\
			size: a4 ;\
			margin: 2.5cm;/*Must be unit cm*/\
			/*===Frame=======*/\
			@frame footer {\
				-pdf-frame-content: simple_text_foot;\
				bottom: 1cm;\
				margin-left: 1cm;\
				margin-right: 1cm;\
				height: 1cm;\
			}\
			@frame header {\
				-pdf-frame-content: simple_text_head;\
				top: 1cm;\
				margin-bottom: 1cm;\
				margin-left: 1cm;\
				margin-right: 1cm;\
				height: 1cm;\
			}\
		}\
		#simple_text_foot {\
		color:rgb(153,157,156)\
		}\
		#simple_text_head {\
		color:rgb(153,157,156)\
		}\
		/*==========Syntax Highligting=========*/\
		.codehilite{background:#fff;}\
		.codehilite .c{color:#998;font-style:italic;}\
		.codehilite .err{color:#a61717;background-color:#e3d2d2;}\
		.codehilite .k{font-weight:bold;}\
		.codehilite .o{font-weight:bold;}\
		.codehilite .cm{color:#998;font-style:italic;}\
		.codehilite .cp{color:#999;font-weight:bold;}\
		.codehilite .c1{color:#998;font-style:italic;}\
		.codehilite .cs{color:#999;font-weight:bold;font-style:italic;}\
		.codehilite .gd{color:#000;background-color:#fdd;}\
		.codehilite .gd .x{color:#000;background-color:#faa;}\
		.codehilite .ge{font-style:italic;}\
		.codehilite .gr{color:#a00;}\
		.codehilite .gh{color:#999;}\
		.codehilite .gi{color:#000;background-color:#dfd;}\
		.codehilite .gi .x{color:#000;background-color:#afa;}\
		.codehilite .go{color:#888;}\
		.codehilite .gp{color:#555;}\
		.codehilite .gs{font-weight:bold;}\
		.codehilite .gu{color:#800080;font-weight:bold;}\
		.codehilite .gt{color:#a00;}\
		.codehilite .kc{font-weight:bold;}\
		.codehilite .kd{font-weight:bold;}\
		.codehilite .kp{font-weight:bold;}\
		.codehilite .kr{font-weight:bold;}\
		.codehilite .kt{color:#458;font-weight:bold;}\
		.codehilite .m{color:#099;}\
		.codehilite .s{color:#d14;}\
		.codehilite .na{color:#008080;}\
		.codehilite .nb{color:#0086B3;}\
		.codehilite .nc{color:#458;font-weight:bold;}\
		.codehilite .no{color:#008080;}\
		.codehilite .ni{color:#800080;}\
		.codehilite .ne{color:#900;font-weight:bold;}\
		.codehilite .nf{color:#900;font-weight:bold;}\
		.codehilite .nn{color:#555;}\
		.codehilite .nt{color:#000080;}\
		.codehilite .nv{color:#008080;}\
		.codehilite .ow{font-weight:bold;}\
		.codehilite .w{color:#bbb;}\
		.codehilite .mf{color:#099;}\
		.codehilite .mh{color:#099;}\
		.codehilite .mi{color:#099;}\
		.codehilite .mo{color:#099;}\
		.codehilite .sb{color:#d14;}\
		.codehilite .sc{color:#d14;}\
		.codehilite .sd{color:#d14;}\
		.codehilite .s2{color:#d14;}\
		.codehilite .se{color:#d14;}\
		.codehilite .sh{color:#d14;}\
		.codehilite .si{color:#d14;}\
		.codehilite .sx{color:#d14;}\
		.codehilite .sr{color:#009926;}\
		.codehilite .s1{color:#d14;}\
		.codehilite .ss{color:#990073;}\
		.codehilite .bp{color:#999;}\
		.codehilite .vc{color:#008080;}\
		.codehilite .vg{color:#008080;}\
		.codehilite .vi{color:#008080;}\
		.codehilite .il{color:#099;}\
		pre {\
		background-color: ghostWhite !important;\
		border: 1px solid #DEDEDE !important;\
		font-size: 12px !important;\
		line-height: 1.5em !important;\
		margin: 1em;\
		overflow: auto !important;\
		padding: 0.5em !important;\
		}\
		/*==========Table of Content=========*/\
		pdftoc {\
			color: #666;\
		}\
		pdftoc.pdftoclevel0 {\
			font-weight: bold;\
			margin-top: 0.5em;\
		}\
		pdftoc.pdftoclevel1 {\
			margin-left: 1em;\
		}\
		pdftoc.pdftoclevel2 {\
			font-style: italic;\
			margin-left:2em;\
		}\
		/*==========Endnotes=========*/\
		.footnote-ref {\
			-pdf-outline: true;\
		}\
		.footnote-ref a {\
			font-weight:bold;\
			text-decoration:none;\
			color:gray;\
		}\
		.footnotes {\
			font-size:86%;\
		}\
		.footnoteBackLink {\
			display:none; /*none to hide ugly bug*/\
		}\
		/*==========Tables=========*/\
		.simple_plain_text th.id, .simple_plain_text td.id {\
			width: 40px;\
		}\
		.simple_plain_text td {\
			width:250px;\
		}\
		.simple_plain_text table {\
			-pdf-keep-in-frame-mode: shrink;\
		}\
		.simple_plain_text th,td.id {\
			background-color:ghostWhite;\
		}\
		.simple_plain_text tr {\
			border: 1px solid #DEDEDE\
		}\
		'
		self.html = '<!DOCTYPE HTML><html><head><title>$title</title>\
						<meta charset="utf-8" /><style type="text/css">$css_file</style></head><body>\
						<table id="simple_text_head"><tr><td>$title</td>\
						<td align="right"><p> $author </p></td></tr></table>\
						<div class="toc"> $simple_toc </div>\
						<div class="simple_plain_text">$plain_text</div>\
						<table id="simple_text_foot"><tr><td><p> $date </p></td>\
						<td align="right"> <p> <pdf:pagenumber> </p> </td></tr></table>\
						</body></html>'
		
	def toString(self):
		from string import Template
		references = self._meta.__dict__.copy()
		references['plain_text'] = self.plain_text
		references['css_file'] = self.css
		references['simple_toc'] = ''
		if "css" in self._meta.__dict__:
			references['css_file'] = get_file_content(meta.css)
			
		if self._meta.toc is True:
			references['simple_toc'] = '<pdf:toc />'
		
		html = Template(self.html).substitute(references)
		return html
		
	def toUnicodeString(self):
		pass

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
	Creates a pdf and saves at destination.
	"""
	import ho.pisa as pisa
	pdfed = pisa.CreatePDF(
        cStringIO.StringIO(html), file(meta.dir + meta.file_name+".pdf", "wb"))

	if pdfed.err:
		print "*** %d ERRORS OCCURED" % pdf.err
	return pdfed
	
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