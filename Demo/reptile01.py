import urllib.request
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/'+str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?author clearfix">.*?<a.*?<img.*?>.*?</a>.*?<div.*?'+
                         'content">(.*?)<!--.*?-->.*?</div>.*?<div class="stats.*?class="number">.*?</i>',re.S)
    items = re.findall(pattern, content)
    print(len(items), 666)
    for item in items:
        print(item)
        # haveimage = re.search('img', item[0])
        # if not haveimage:
        #     print(item[0])
except urllib.request.URLError as e:
    print('except:', e)

