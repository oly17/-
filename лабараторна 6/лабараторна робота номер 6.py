from bs4 import BeautifulSoup
import requests
from collections import Counter
from lxml import html
from string import punctuation

r = requests.get("https://rozetka.com.ua/promo/banner_black-friday/?gclid=Cj0KCQiA7oyNBhDiARIsADtGRZY1MhzkaIXpG7hrH2UdegyIfPuGkN7vUoO_Uz_HrGC8KA8P3KKB3_gaApWSEALw_wcB")
soup = BeautifulSoup(r.text, 'html.parser')
links = [a['href'] for a in soup.find_all('a')]
print('Ссылки на странице:')
for i in links:
    print(i)
    count = len(links)
print('Количество ccылок: {}'.format(count))

images = soup.find_all('img')
print ('Количество изображений:', len(images))

text = (''.join(s.findAll(text=True))for s in soup.findAll('p'))
counter = Counter(x.rstrip(punctuation).lower() for y in text for x in y.split())
print('Подсчёт разных слов:', counter.most_common())

cont = html.fromstring(r.content)
items = cont.cssselect('*')
tags = [x.tag for x in items]
c = Counter(tags)
print ('Теги на странице:', repr(c).strip('Counter'))