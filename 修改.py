from selenium import webdriver
import time
from fake_useragent import UserAgent
from urllib.parse import quote
from selenium.webdriver.chrome.options import Options
import requests


def set_headless_chrome():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def main():
    list = []
    key = quote(input('请输入想要下载的歌曲：\n'))
    driver = set_headless_chrome()
    url = 'https://music.163.com/#/search/m/?s={}&type=1'.format(key)
    driver.get(url)
    driver.switch_to.frame('g_iframe')
    req = driver.find_element_by_id('m-search')
    a_id = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//a').get_attribute("href")
    print('原网站地址：')
    print(a_id)
    song_id = a_id.split('=')[-1]
    list.append(song_id)
    # print(song_id)
    song_name = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//b').get_attribute("title")
    list.append(song_name)
    print(song_name)
    time.sleep(2)
    print('%s'%song_name + '已经开始下载')
    driver.quit()
    # print(list)
    get_content(list)


def get_content(list):
    base_url = 'https://music.163.com/song/media/outer/url?id='
    id = list[0]
    url = base_url + id
    title = list[1]
    headers = {
        'User-Agent' : UserAgent().random
    }
    req = requests.get(url,headers = headers,timeout = 30).content
    with open('D:\wangyiyunmusic\%s.mp3'%title,'wb') as f:
        f.write(req)
        print('%s'%title + '已经下载到D:\wangyiyunmusic文档中')
        time.sleep(2)
    main()






























if __name__ == '__main__':
    main()