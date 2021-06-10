import requests
import re
from fake_useragent import UserAgent
import time

headers = {
    'User-Agent' : UserAgent().random
}

url = 'https://www.baidu.com/'

req = requests.get(url,headers = headers,timeout = 30).text
time.sleep(3)
print(req)

