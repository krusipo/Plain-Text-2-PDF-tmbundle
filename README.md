## About
A TextMate bundle to create styled PDFs from source code and documentation.

### Code to PDF.
The User works on a project in TextMate and wants to have a pdf of source code,
she selects the Plain Text to PDF bundle and menu option: "Code to PDF" seconds 
later a PDF with line numbering and syntax highlighting exists open in Preview.

### Plain to PDF
The User has created a README.md for a project and wants to share the 
contents of the README with a non-techy individual. He selects the Plain Text 
to PDF bundle  and menu option: "Plain to PDF" seconds later a PDF is created 
at the project paths root, tailored with options from emac styled comment variables. 

#### Usage
// Instructions here

## Installation 

When dependencies (see below) are met. // write shell install script.
   * Install from git
   // Instructions here

   * Install without git
   // Instructions here 

### Dependencies
**Plain to PDF:** requires the following eggs the ones marked optional 
wont break functionality if not present, but stuff will behave strange.

 * [python-markdown2](http://code.google.com/p/python-markdown2/)
	 - [pygments (optional)](http://pygments.org/)
 * [xhtml2pdf](https://github.com/holtwick/xhtml2pdf)
     - [Reportlab Toolkit 2.2+](http://www.reportlab.org/)
     - [html5lib 0.11.1+](http://code.google.com/p/html5lib/)
     - [pyPdf 1.11+ (optional)](http://pybrary.net/pyPdf/)

**Code to PDF:** uses [Vim](http://www.vim.org/) do all the heavy lifting 
so *.vimrc* needs to be set up to support colorschemes, line-numbers, and
other eye-candy.

	In ~/.vimrc add
	set printoptions=number:y "Show line-numbers on print
	set printfont=courier:h9 "Use courier as font
	set syntax on

### Standalone Plain to PDf
The Plain to PDF functionality is available as a standalone CLI-based app,
just download that file and use it as below after dependencies are met.
$ python markdown2pdf.py -h, --help
	# print help, then exit.

$ python markdown2pdf.py -f, --file
	# Create PDF with defaults from file.
				
## TO-DO 
    * Finish the bundle
    * Write install script for eggs