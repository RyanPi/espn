### this is a simple script used to parse espn.com for the top
### headlines of the day.

import requests
from bs4 import BeautifulSoup

#get the page and store the page content
response = requests.get("http://www.espn.com")
content = response.content

#use BeautifulSoup to load content for parsing
soup = BeautifulSoup(content, 'html.parser')
#get the headline header and print the header
top_headlines = soup.select(".module__header")
print(top_headlines[0].text +": ")
#get the headline text and print the text
headlines = soup.select(".headlineStack__list li a")
#use a simple incrementer for number formatting

for count,li in enumerate(headlines, start=1):
    print(str(count) + ". " + li.text)
