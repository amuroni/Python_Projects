"""This app will change a plain text file content into a marked up language such as HTML.
It needs to classify various text elements and clearly mark them
"""

import sys
import re  # regular expressions module needed!


# collect lines
def lines(file):
    for line in file: yield line
    yield "\n"


# collect lines until you find an empty line, then call it a block
def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield "".join(block).strip()
            block = []


print('<html><head><title>...</title><body>')

title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)*', r'<em>\1</em>', block)
    if title:
        print("<h1>")
        print(block)
        print("</h1>")
        title = False
    else:
        print("<p>")
        print(block)
        print("</p>")

print('</body></html>')
