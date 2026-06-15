
from bs4 import BeautifulSoup
import requests

# Run once!
# url = "https://www.google.com/about/careers/applications/jobs/results"

# response = requests.get(url)

# with open("Web Scraping\google_jobs.html", "w", encoding="utf-8") as file:
#     file.write(response.text)

# print("HTML saved!")


#Scraping code

soup = BeautifulSoup('Web Scraping\google_jobs.html', 'lxml')



print(soup.prettify())


# li class_ = '1Ld3Je'
# title = h3

#location =
# span class_ = 'pwO9Dc vo5qdf' -> spans

# div = 'Xsxa1e' - li  -> minimum qualifications

# div = 'VfPpkd-dgl2Hf-ppHlrf-sM5MNb' - a -> href = Learn more/ job link
