from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
import time
class Download(object):
    def __init__(self):
        self.url = 'https://lovelive.tools/'
    def set_headless_chrome(self):
        """
        设置无头浏览器
        :return: driver
        """
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options = chrome_options)
        # driver = webdriver.Chrome()
        return driver

    def web_content(self,driver):
        driver.get(self.url)
        page_source = driver.page_source
        e = etree.HTML(page_source)
        content = e.xpath('//*[@id="root"]/div/div[2]/div/div/div/div/div/div[1]/div[2]/text()')
        print(content)
        time.sleep(10)

if __name__ == '__main__':
    d = Download()
    driver = d.set_headless_chrome()
    d.web_content(driver)
