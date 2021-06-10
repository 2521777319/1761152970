import requests
#from lxml import etree
from lxml import html

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}
for a in range(5):
    url = 'https://book.douban.com/top250?start={}'.format(a*25)
    data = requests.get(url,headers = headers).text
    etree = html.etree
    s=etree.HTML(data)
    #file用来记录循环次数
    file=s.xpath('//*[@id="content"]/div/div[1]/div/table')
    #通过@title获取他的title标签里面的内容

    for info in file:
        title = info.xpath('./tr/td[2]/div[1]/a/@title')[0]
        href = info.xpath("./tr/td[2]/div[1]/a/@href")[0]
        score = info.xpath('./tr/td[2]/div[2]/span[2]/text()')[0]
        #只取评论的第一条
        commitmentNum=info.xpath('./tr/td[2]/div[2]/span[3]/text()')[0].strip("(").strip().strip(")")
        scribe=info.xpath("./tr/td[2]/p[2]/span/text()")
        #防止没有评论出现
        if len(scribe) > 0:
            print("{}     {}     {}     {}     {}\n".format(title,href,score,commitmentNum,scribe[0]))
        else:
            print("{}     {}     {}     {}\n".format(title,href,score,scribe))

