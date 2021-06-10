import requests
from fake_useragent import UserAgent
from lxml import etree
# import io
# import sys
import time

def get_htmls(headers,recreat_url):
    req = requests.get(recreat_url,headers = headers,timeout = 30)
    req.encoding = 'utf-8'
    print(req.text)
    return req.text
def get_urls():
    pass
def parse_urls():
    pass
def get_contents():
    pass
def save():
    pass
def main():
    headers = {
        'User-Agent' : UserAgent().random
    }
    official_url = ''
    recreat_url = ''
    get_htmls(headers,recreat_url)
    time.sleep(5)
if __name__ == '__main__':
    main()