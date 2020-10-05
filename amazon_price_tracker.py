import requests
from bs4 import BeautifulSoup

URL=input("Enter the URL of the product on Amazon.")

headers={"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.1 Safari/605.1.15'}

page=requests.get(URL, headers=headers)

soup=BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())