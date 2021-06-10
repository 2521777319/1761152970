import requests
from fake_useragent import UserAgent

headers = {
    "User_Agent" : UserAgent().random
}

url = 'https://www.baidu.com/s?'

#设置代理


#在连接上面追加搜索内容
name = input("请输入想要搜索的页面:")
params = {
    "wd" : name
}

req = requests.get(url,headers = headers,params = params,timeout = 3).text
print(req.encode())


