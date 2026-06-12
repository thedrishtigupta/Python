
from bs4 import BeautifulSoup
import requests

with open("Web Scraping\simple.html") as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())

# match = soup.title.text
# print(match)

# match = soup.div #gives first div on page
# print(match)

# match = soup.find('div', class_='footer') #helps finding specific div, with class or id
# print(match)

# article = soup.find('div', class_ = 'article')
# # print(article)

# headline = article.h2.a.text
# print(headline)

# summary = article.p.text
# print(summary)

for article in soup.find_all('div', class_ = 'article'):
    headline = article.h2.a.text
    summary = article.p.text
    print(headline)
    print(summary)
    print()