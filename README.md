# DOCX to LaTeX Converter

This Python script, `docx_to_latex_converter.py`, converts a DOCX (Microsoft Word) document into a LaTeX file.

## Features

- Converts plain text from a Word document to LaTeX format.
- Handles simple text formatting like bold, italic, and underline.

## Prerequisites

To run this script, you'll need:

- Python 3.x
- `python-docx` library

Python can be downloaded from the official website, and `python-docx` can be installed via pip:

## Installation
Make sure Python and pip are installed on your system and are available in your command line path.

Install the necessary Python package python-docx by running the following command:

```
pip install python-docx
```
## Usage
Place your .docx file in the same directory as the script or specify the path to your .docx file.

Update the script with the paths to your .docx file and where you want to save the .tex file.

Run the script using Python in your terminal or command prompt:
`python docx_to_latex_converter.py`

This will generate a .tex file with the converted content.

## Customization
This script is a starting point for DOCX to LaTeX conversion. It may require customization for complex documents with elements like tables, images, equations, etc.

## Limitations
The script does not support complex elements like tables, images, equations, or sophisticated formatting. Additional development and manual adjustments may be required for such cases.
