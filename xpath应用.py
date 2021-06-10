import requests
from lxml import etree



#//*[@id="wrapper"]/h1/span
#//*[@id="link-report"]/div[1]/div/p



headers = {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}


url = 'https://book.douban.com/subject/30389935/'
req = requests.get(url,headers = headers).text
res = etree.HTML(req)
#print(res)
Name = res.xpath('//*[@id="wrapper"]/h1/span/text()')[0]
Content = res.xpath('//*[@id="content"]/div/div[1]/div[3]/h2[1]/span/text()')[0]
Content1 = res.xpath('//*[@id="link-report"]/div[1]/div/p/text()')[0]
autor = res.xpath('//*[@id="content"]/div/div[1]/div[3]/h2[2]/span/text()')[0]
autor1 = res.xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div/div/p/text()')[0]
catalog = res.xpath('//*[@id="content"]/div/div[1]/div[3]/h2[3]/span/text()')[0]
catalog1 = res.xpath('//*[@id="dir_30389935_full"]/text()')[0]
Comment = res.xpath('//*[@id="comments"]/ul/li[3]/div/p/span/text()')[0]

print('{}\n'.format(Name),'{}:{}\n'.format(Content,Content1))
print('{}:{}\n'.format(autor,autor1))
print('{}:{}\n'.format(catalog,catalog1))
print(Comment)

