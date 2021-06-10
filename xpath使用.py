import requests
from lxml import etree
from fake_useragent import UserAgent

headers1 = {
    'User-Agent' : UserAgent().random
}

#//*[@id="list"]/dl/dd[1]/a
url = 'http://www.xbiquge.la/14/14930/'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}

#链接爬取
req = requests.get(url,headers = headers,timeout = 30).text
res = etree.HTML(req)
#print(res)
address = res.xpath('//*[@id="list"]/dl/dd/a/@href')
i = 0
html = []
for add in address:
    web = 'http://www.xbiquge.la' + add.strip()
    html.append(web)
    # print(html)
    i+=1
    ChapterNumber = ["第" + str(i) + "章"]
    print(ChapterNumber)
    # with open('html','a',encoding = 'utf-8') as f:
    #     f.write(html + '\n' + ChapterNumber)


#小说标题和内容爬取
#//div[@class="bookname"]/h1
#//*[@id="content"]
for num in range(i):
    requ = requests.get(html[num],headers = headers1,timeout = 30).text
    resp = etree.HTML(requ)
    title = resp.xpath('//div[@class="bookname"]/h1/text()')[0]
    content = resp.xpath('//*[@id="content"]/text()')[:]
    for n in content:
        print(n)
# with open('yuanzun', 'a', encoding='utf-8') as p:
#     p.write(title+ '\n')
#     p.writelines(i)
#     p.write('\n\n')
#写入操作就先不管了，我要开始BeautifulSoup的学习了，哈哈哈哈，xpath到此（不要忘记Chrome浏览器的xpath小插件，超级好用的哦）