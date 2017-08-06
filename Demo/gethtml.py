import urllib.request
import urllib.parse
import re

def getHtml():
    request = urllib.request.Request('https://tieba.baidu.com/index.html')
    page = urllib.request.urlopen(request)
    return page.read()


def getImage(htmls):
    reg = r'img src="(https://.+?\.jpe?g)'''
    image = re.compile(reg)
    htmls=htmls.decode('UTF-8', 'ignore')
    imagelist = re.findall(image, htmls)
    x = 0
    b = b'/:?='
    for im in imagelist:
        print(im)
        # urllib.request.urlretrieve(urllib.parse.quote(im[2:], b), 'D:\pythonProject\image\%s.jpg' % x)
        x+=1
    return x

html = getHtml()
print(getImage(html))
print('finished')

