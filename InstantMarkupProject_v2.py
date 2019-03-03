"""Uses the classes from v1, condensed into a single file for more readable code"""

import sys
import re


# 0 - basic functions for lines and block
def lines(file):
    for line in file:
        yield line
    yield "\n"


def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield "".join(block).strip()
            block = []


# 1 - the handler
class Handler:

    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)
        if callable(method): 
            return method(*args)

    def start(self, name):
        self.callback('start_', name)

    def end(self, name):
        self.callback('end_', name)

    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None: 
                match.group(0)
            return result
        return substitution


# 2 - the HTML renderer
class HTMLRenderer(Handler):

    @staticmethod
    def start_document():
        print('<html><head><title>...</title></head><body>')

    @staticmethod
    def end_document():
        print('</body></html>')

    @staticmethod
    def start_paragraph():
        print('<p>')

    @staticmethod
    def end_paragraph():
        print('</p>')

    @staticmethod
    def start_heading():
        print('<h2>')

    @staticmethod
    def end_heading():
        print('</h2>')

    @staticmethod
    def start_list():
        print('<ul>')

    @staticmethod
    def end_list():
        print('</ul>')

    @staticmethod
    def start_listitem():
        print('<li>')

    @staticmethod
    def end_listitem():
        print('</li>')

    @staticmethod
    def start_title():
        print('<h1>')

    @staticmethod
    def end_title():
        print('</h1>')

    @staticmethod
    def sub_emphasis(match):
        return '<em>{}</em>'.format(match.group(1))

    @staticmethod
    def sub_url(match):
        return '<a href="{}">{}</a>'.format(match.group(1), match.group(1))

    @staticmethod
    def sub_mail(match):
        return '<a href="mailto:{}">{}</a>'.format(match.group(1), match.group(1))

    @staticmethod
    def feed(data):
        print(data)


# 3 - Rules
class Rule:

    def __init__(self, type):
        self.type = type

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True


class HeadingRule(Rule):
    type = "heading"

    def condition(self, block):
        return "\n" not in block and len(block) <= 70 and not block[-1] == ":"


class TitleRule(HeadingRule):
    type = "title"
    first = True

    def condition(self, block):
        if not self.first:
            return False
        self.first = False
        return HeadingRule.condition(self, block)


class ListItemRule(Rule):
    type = "listitem"

    def condition(self, block):
        return block[0] == "-"

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True


class ListRule(ListItemRule):
    type = "list"
    inside = False  # states if the parser currently in a list or not

    def condition(self, block):
        return True  # if true, the parser is in a list

    def action(self, block, handler):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)
            self.inside = True  # in a list
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False


class ParagraphRule(Rule):
    type = "paragraph"

    @ staticmethod
    def condition():
        return True


# 4 - the Parser

class Parser:

    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def add_filter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        self.handler.start("document")
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last:
                        break
        self.handler.end("document")


class BasicTextParser(Parser):
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.add_rule(ListRule(type))
        self.add_rule(ListItemRule(type))
        self.add_rule(TitleRule(type))
        self.add_rule(HeadingRule(type))
        self.add_rule(ParagraphRule(type))
        self.add_filter(r'\*(.+?)\*', 'emphasis')
        self.add_filter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.add_filter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')


# 5 - assign handler and parser to each class and call the parser
handler = HTMLRenderer()
parser = BasicTextParser(handler)

parser.parse(sys.stdin)

# for some reason it doesn't work despite adding all expect classes etc.
# seems like the example in the book is poorly coded, will discard this for now
# useful only for certain aspects of class building, the actual result is not very clear
