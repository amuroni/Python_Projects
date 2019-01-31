# from lxml import html
#
# import requests
#
# page = requests.get("https://diretta.frequence-radio.com/frequenza-radio-lazio.html")
# tree = html.fromstring(page.content)
#
# test = tree.xpath('//div[@id="radios_listing"]/text()')
# print(test)  # doesn't seem to work properly, no actual value printed

# this time is better to try with BeautifulSoup, already installed
# commented out the first part since I won't be using it again
# for future reference and tests see: https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe