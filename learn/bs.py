from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

base_url = 'https://baike.baidu.com'
his = ['/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711']
num = random.randint(1, 20)

for i in range(num):
    html = urlopen(base_url + his[-1]).read().decode('UTF-8')
    soup = BeautifulSoup(html, features='lxml')
    href = soup.find_all('a', {'href': re.compile('/item/(%.{2})+$')})
    print(len(href))
    href = [l['href'] for l in href]
    if not href:
        his.pop()
    else:
        his.append(random.choice(href))

print(base_url + his[-1])
