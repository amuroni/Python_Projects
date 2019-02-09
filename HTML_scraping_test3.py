import requests
import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate

# we load the url from which we will scrape the data
page = requests.get("https://diretta.frequence-radio.com/frequenza-radio-campania.html")

soup = BeautifulSoup(page.content, "lxml")   # let BSoup load the raw html with html.parser
table = soup.findAll("table")[0]  # get the table from the htlm raw
df = pd.read_html(str(table))     # read the str items in the table

print(tabulate(df[0], headers="keys", tablefmt="psql"))  # use  module tabulate to get a nice, usable printout
