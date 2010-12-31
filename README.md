## About
A TextMate bundle to create styled PDFs from source code and documentation.

## Use-cases
### Code to PDF.
The User works on a project in TextMate and wants to have a pdf of source code,
she selects the Plain Text to PDF bundle and menu option: "Code to PDF" seconds 
later a PDF with line numbering and syntax highlighting exists open in Preview.

### Plain to PDF
The User has created a README.md for a project and wants to share the contents 
of the README with a non-techy individual. He selects the Plain Text to PDF bundle 
and menu option: "Plain to PDF" seconds later a PDF is created at the project paths
root, tailored with options from emac styled comment variables.


## Dependencies (Plain to PDF)
 * [python-markdown2](http://code.google.com/p/python-markdown2/)
	 - [pygments](http://pygments.org/)
 * [xhtml2pdf](https://github.com/holtwick/xhtml2pdf)
     - [Reportlab Toolkit 2.2+](http://www.reportlab.org/)
     - [html5lib 0.11.1+](http://code.google.com/p/html5lib/)
     - [pyPdf 1.11+ (optional)](http://pybrary.net/pyPdf/)

	Requirements

	.vimrc needs to be set up to support colorschemes, line-numbers, and other eye-candy.

	In ~/.vimrc add
	set printoptions=number:y "Show line-numbers on print
	set printfont=courier:h9 "Use courier as font
	set syntax on

	### Usage
			$ python markdown2pdf.py -h, --help
				# print help, then exit.

			$ python markdown2pdf.py -f, --file
				# Create PDF with defaults from file.