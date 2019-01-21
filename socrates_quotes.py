import requests
from bs4 import BeautifulSoup
import sys
import io
import re
from time import sleep
from csv import writer, reader

soc_quotes = []
soc_bio = []
base_url = "https://www.keepinspiring.me/socrates-quotes/"

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def scrape(quotes, bio):
    res = requests.get(f"{base_url}")
    print(f"Now Scraping {base_url}")
    soup = BeautifulSoup(res.text, "html.parser")
    # Socrates Quotes
    quote_all = soup.find_all(class_ = "author-quotes")
    for i in range(len(quote_all)):
        quote = quote_all[i].get_text()
        quote = quote.replace("\n", "")
        quote = quote.replace("-Socrates", "")
        quote = quote.replace("\'", "")
        soc_quotes.append(quote)
    # Socrates Bio
    main_div = soup.find(class_ = "main fix sidebar-right")
    bio_counter = 0
    for child in main_div.stripped_strings:
        child = child.replace("\xa0", "")
        soc_bio.append(child)
        bio_counter += 1
        if bio_counter == 5:
            break
    return quotes, bio

def write_bio(bio):
    with open("soc_bio.csv", "wb") as file:
        for b in bio:
            file.write(b.encode("utf-8"))

## utf-8 is definitely needed for the quotes as ascii can't recognize all of the characters
def write_quote(quotes):
    with open("soc_q.csv", "wb") as file:  ###  WHEN ENCODING IN UTF-8 NEED TO HAVE "WB" WRITE BYTES
        for q in quotes:
            file.write(q.encode("utf-8"))

def read(filename):
    soc = []
    with open(filename, 'rb') as file:
        for line in file:
            line = line.decode("utf-8")
            soc.append(line)
    return soc

quotes, bio = scrape(soc_quotes, soc_bio)
write_quote(quotes)
write_bio(bio)
soc = read("soc_q.csv")
b = read("soc_bio.csv")
print(b)
print(soc)
# print(read_quote(quotes))
# print(read_bio(bio))
