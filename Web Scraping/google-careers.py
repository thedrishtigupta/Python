
from bs4 import BeautifulSoup
import requests

# Run once!
# url = "https://www.google.com/about/careers/applications/jobs/results"

# response = requests.get(url)

# with open("Web Scraping/google_jobs.html", "w", encoding="utf-8") as file:
#     file.write(response.text)

# print("HTML saved!")


#Scraping code

with open("Web Scraping/google_jobs.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "lxml")



# print(soup.prettify())

job_title = soup.find('li', class_='1Ld3Je')
print(job_title)


# li class_ = '1Ld3Je'
# title = h3

#location =
# span class_ = 'pwO9Dc vo5qdf' -> spans

# div = 'Xsxa1e' - li  -> minimum qualifications

# div = 'VfPpkd-dgl2Hf-ppHlrf-sM5MNb' - a -> href = Learn more/ job link
