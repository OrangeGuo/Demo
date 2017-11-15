from bs4 import BeautifulSoup
import requests
target = 'http://www.biqukan.com/1_1094/5403177.html'
req = requests.get(url=target)
bf = BeautifulSoup(req.text,'lxml')
texts = bf.find_all('div',class_='showtxt')
print(texts[0].text.replace('\xa0'*8,'\n\n'))
