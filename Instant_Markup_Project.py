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


# making a first test of the script to ensure it works properly

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


# time to define some classes/objs to make the program modular as intended

# handler superclass

class Handler:

    def callback(self, prefix, name, *args):  # used to find the correct method given the prefix
        method = getattr(self, prefix + name, None)  # getattr with None as default
        if callable(method): return method(*args)  # if callable, call with all args supplied

    def start(self, name):  # helper method - calls start prefix
        self.callback("start_", name)

    def end(self, name):  # helper method - calls end prefix
        self.callback("end_", name)

    def sub(self, name):  # returns a new function
        def substitution(match):  # it's a re.sub statement basically
            result = self.callback("sub_", name, match)
            if result is None: match.group(0)
            return result
        return substitution


# time to implement the actual parsing of the original text.
# we need rules as a separate object
# here is an example of the rule class which we'll use for this project:

class Rule:  # calls the start/end method of the handler with type string arg (which all subclasses need to work)

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True


# definition of the Parser class, which uses the handler and the rules to filter & transform the txt in mark up

class Parser:

    def __init__(self, handler):  # initializes the attr handler and 2 lists, rules and filters
        self.handler = handler
        self.rules = []
        self.filters = []

    def addrule(self, rule):  # the rule method adds a rule to the rules list
        self.rules.append(rule)

    def addfilter(self, pattern, name):  # creates a filter and adds it to the list of filters
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        self.handler.start("document")  # calls the document
        for block in blocks(file):  # iterates over all the file blocks
            for filter in self.filters:  # applies the filters
                block = filter(block, self.handler) # calls the filter function to apply filters
            for rule in self.rules:  # applies the rules
                if rule.condition(block):
                    last = rule.action(block, self.handler)  # calls the rules function to apply rules
                    if last:
                        break
        self.handler.end("document")


class BasicTextParser(Parser):
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addrule(ListRule())
        self.addrule(ListItemRule())
        self.addrule(TitleRule())
        self.addrule(HeadingRule())
        self.addrule(ParagraphRule())



# time to create the first rule: heading.
# the heading rule checks that:
# - the block does not contain a new line (\n),
# - the length is at least 70 char
# - the last char is not a colon.

class HeadingRule(Rule):
    type = "heading"

    def condition(self, block):
        return not "\n" in block and len(block) <= 70 and not block[-1] == ":"


# then we add a list item rule, as follows
class ListItemRule(Rule):
    type = "listitem"

    def condition(self, block):
        return block[0] == "-"  # the first char must be a "-", as in a bullet list

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())  # get the item removing the first char ("-") from the block
        handler.end(self.type)
        return True


# we need another rule for the list item
# a list begins after a block item, and ends after the last list item
class ListRule(ListItemRule):
    type = "list"
    inside = False  # states if the parser currently in a list or not

    def condition(self, block):
        return True  # if true, the parser is in a list

    def action(self, block, handler):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)
            self.inside = True  # in a list
        elif self.inside and not ListItemRule.condition(self.block):
            handler.end(self.type)
            self.inside = False
        return False


# and finally, the paragraph rule which is the simpler one
# it is always true since works as default, everything that is not a list/heading is a <p>...</p>
class ParagraphRule(Rule):
    type = "paragraph"

    def condition(self, block):
        return True


# to simpliftythe Handler, we create a specific html render, to implement basic HTML markup
# it basically contains all title, paragraph and list items
# uses the methods of the Handler superclass
class HTMLRenderer(Handler):

    def start_document(self):
        print('<html><head><title>...</title></head><body>')

    def end_document(self):
        print('</body></html>')

    def start_paragraph(self):
        print('<p>')

    def end_paragraph(self):
        print('</p>')

    def start_heading(self):
        print('<h2>')

    def end_heading(self):
        print('</h2>')

    def start_list(self):
        print('<ul>')

    def end_list(self):
        print('</ul>')

    def start_listitem(self):
        print('<li>')

    def end_listitem(self):
        print('</li>')

    def start_title(self):
        print('<h1>')

    def end_title(self):
        print('</h1>')

    def sub_emphasis(self, match):
        return '<em>{}</em>'.format(match.group(1))

    def sub_url(self, match):
        return '<a href="{}">{}</a>'.format(match.group(1), match.group(1))

    def sub_mail(self, match):
        return '<a href="mailto:{}">{}</a>'.format(match.group(1), match.group(1))

    def feed(self, data):
        print(data)
