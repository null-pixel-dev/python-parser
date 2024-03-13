from docx import Document

def parse_paragraph(paragraph):
    """Parse a paragraph to return LaTeX formatted text."""
    text_runs = []
    for run in paragraph.runs:
        text = run.text.replace('&', '/&').replace('%', '/%').replace('_', '/_').replace('#', '/#')
        if run.bold:
            text = '\\textbf{' + text + '}'
        if run.italic:
            text = '\\textit{' + text + '}'
        if run.underline:
            text = '\\underline{' + text + '}'
        text_runs.append(text)
    return ' '.join(text_runs)

def docx_to_tex(docx_path, tex_path):
    """Convert a DOCX file to a TEX file."""
    document = Document(docx_path)
    with open(tex_path, 'w', encoding='utf-8') as tex_file:
        for paragraph in document.paragraphs:
            tex_file.write(parse_paragraph(paragraph) + '\n\n')

# Use the function to convert a document
docx_path = './Lab_2_-_G78.docx'
tex_path = './Lab2-G78.tex'
docx_to_tex(docx_path, tex_path)
