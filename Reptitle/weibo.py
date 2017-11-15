from bs4 import BeautifulSoup
import requests
target = 'https://weibo.com/u/5643757769/home'
req = requests.get(url=target)
bf = BeautifulSoup(req.text,'lxml')
texts = bf.find_all('div',class_='showtxt')
print(texts[0].text.replace('\xa0'*8,'\n\n'))
