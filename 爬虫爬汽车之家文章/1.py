import requests
from bs4 import BeautifulSoup

# 下载页面
ret = requests.get(
    url="https://www.autohome.com.cn/news/"
)
ret.encoding = ret.apparent_encoding
# print(ret.text)
# 页面解析，获取指定内容
soup = BeautifulSoup(ret.text, 'html.parser')
div = soup.find(name='div', id='auto-channel-lazyload-article')
li_list = div.find_all(name='li')
for li in li_list:
    h3 = li.find(name='h3')
    if not h3:
        continue
    # print(h3.text,"\t")
    p = li.find(name='p')
    a = li.find(name='a')
    # print(a.attrs)
    print(h3.text, a.get('href'))
    print(p.text)

    img = li.find('img')
    src = img.get('src')

    file_name = src.rsplit('__', maxsplit=1)[1]
    print(file_name)
    print('=' * 100)
    ret_img = requests.get(url='https:' + src)
    with open(file_name, 'wb') as f:
        f.write(ret_img.content)