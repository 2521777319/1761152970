import requests
from fake_useragent import UserAgent
import time
import re
import json
from lxml import etree



def response_urls(url):
    """

    :rtype: object
    """
    headers = {
        'User-Agent' : UserAgent().random,
        'Cookie' : ''
    }
    s = requests.session()
    req = s.get(url,headers = headers,timeout = 30)
    time.sleep(3)
    # print(req)
    return req.json()

#//*[@id="J_section_0"]/div/div/div/div/div[1]/a/span
#//*[@id="J_section_1"]/div/div/div/div/div[1]/a/span
#//*[@id="J_section_2"]/div/div/div/div/div[1]/a/span
#//span [@class="J_title"]

def prase_html(html):
    jsons = json.loads(html.text)
    e = etree.HTML(str(jsons))
    h = etree.tostring(e)
    return h.decode('utf-8')



if __name__ == '__main__':
    url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=20&format=json&keyword=%E6%AD%A6%E6%B1%89%E8%82%BA%E7%82%8E&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1579680690648'
    html2 = response_urls(url)
    html = prase_html(html2)
    print(html)
    # prase_html(html)

    # print(html)