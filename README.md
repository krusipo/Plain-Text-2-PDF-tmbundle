## About
Module **produces** a styled easy readable PDF by converting 
markdown formatting to html and then target the DOM elements
with applicable CSS.

This is a paragraph with a footnote. [^1]

[^1]: 1. This is the text of the note.

## Usecase
 User works on a project in Textmate and creates a README.md then
 he selects the mate2pdf bundle and menu option: "Create PDF from 
 Readme"

 PATH to the README will always be passed as an argument.
 
 User may then find his styled readme.pdf in same folder as project.

### Usage
		$ python markdown2pdf.py -h, --help
			# print help, then exit.
		
		$ python markdown2pdf.py -f, --file
			# Create PDF with defaults from file.


## Dependencies
 * [python-markdown2](http://code.google.com/p/python-markdown2/)
	 - [pygments](http://pygments.org/)
 * [xhtml2pdf](https://github.com/holtwick/xhtml2pdf)
     - [Reportlab Toolkit 2.2+](http://www.reportlab.org/)
     - [html5lib 0.11.1+](http://code.google.com/p/html5lib/)
     - [pyPdf 1.11+ (optional)](http://pybrary.net/pyPdf/)



