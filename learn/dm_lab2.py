from typing import List
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")
quote_list = soup.find_all("div", class_='quote')
answer = []
for item in quote_list:
    i = []
    author = item.find("small", class_="author")
    i.append({"author": author.text})
    poem = item.find("span", class_="text")
    i.append({"poem": poem.text})
    tag = item.find("meta", class_="keywords")
    i.append({"tag": tag.get("content")})
    answer.append(i)
print(answer)
