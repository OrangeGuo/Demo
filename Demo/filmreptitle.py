import urllib.request
import re
import random
# 用户代理
USER_AGENTS = [ "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
                "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
                "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
                "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
                "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
                "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
                "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
                "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
                "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
                "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
                "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
                "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
                "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20", "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52", ]



def gethref(url_temp):
    # print(url_temp)
    user_agent = random.choice(USER_AGENTS)
    request_temp = urllib.request.Request(url_temp, headers={ 'User-Agent' : user_agent })
    response_temp = urllib.request.urlopen(request_temp)
    content_temp = response_temp.read().decode('gbk')
    # print(content_temp)
    pattern_temp = re.compile('<div.*?<td.*?>.*?<a href=.*?ftp:(.*?)">',re.S)
    href = re.findall(pattern_temp, content_temp)
    return href

def getFileList(page):
    try:
        if page == 1:
            url = 'http://www.dytt8.net/html/gndy/dyzz/index.html'
        else:
            url = 'http://www.dytt8.net/html/gndy/dyzz/list_23_' + str(page) + '.html'
        user_agent = random.choice(USER_AGENTS)
        request = urllib.request.Request(url, headers={'User-Agent': user_agent})
        response = urllib.request.urlopen(request)
        content = response.read().decode('gbk', 'ignore')
        pattern = re.compile('<table.*?<b>.*?<a href="(.*?)" class="ulink">(.*?)</a>.*?</table>', re.S)
        items = re.findall(pattern, content)
        index = 1
        for item in items:
            print(str(index) + '片名:' + item[1])
            index += 1
            # print('ftp:'+str(gethref('http://www.dytt8.net'+item[0])[0]))
        page += 1
    except urllib.request.URLError as e:
        print('except:', e)
    return page

if __name__ == '__main__':
    page = 1
    page = getFileList(page)
    while input('输入回车继续:') == '':
        page = getFileList(page)
