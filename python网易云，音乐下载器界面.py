#-*- coding: utf-8 -*-
import os
from urllib.request import urlretrieve
import requests
from fake_useragent import UserAgent
import time
from selenium import webdriver
# 界面
from tkinter import *
# 窗口创建
root = Tk()
# 添加标题
root.title('网易云音乐下载器')
# 设置窗口大小 //不设置就是默认大小
root.geometry('560x450')
# 标签控件  text即文本内容 font就是字体
label = Label(root,text = '请输入歌曲名称：',font = ('幼圆',20))
# 标签放置位置
label.grid()
# 输入框
entry = Entry(root,font = ('宋体',20))
entry.grid(row = 0,column  = 1)
# 列表框
text = Listbox(root,font = ('楷书',16),width = 50,heigh = 15)
text.grid(row = 1,columnspan = 2)
# 开始按钮
button = Button(root,text = '开始下载',font = ('幼圆',15),command=main)
button.grid(row = 2,column = 0,sticky = W)
# 退出按钮
button1 = Button(root,text = '退出程序',font = ('幼圆',15),command = root)
button1.grid(row = 2,column = 1,sticky = E)

# 显示界面
root.mainloop()


#https://music.163.com/#/search/m/?s=%E7%82%B8%E5%B1%B1&type=1
#https://m10.music.126.net/20200204131604/23f9ea342c6c5cdc9f926b3e67b714d9/yyaac/0409/025d/005b/3cd60d035f5744e47c5c7197dba9d3bd.m4a
#http://music.163/song/media/outer/url?id=574566207.mp3

#搜索名称
from selenium.webdriver.chrome.options import Options


def set_headless_chrome():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def main():
    name = entry.get()
    driver = set_headless_chrome()
    url = 'https://music.163.com/#/search/m/?s={}&type=1'.format(name)
    driver.get(url)
    driver.switch_to.frame('g_iframe')
    req = driver.find_element_by_id('m-search')
    a_id = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//a').get_attribute("href")
    print(a_id)
    song_id = a_id.split('=')[-1]
    print(song_id)
    song_name = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//a').get_attribute("title")
    print(song_name)
    item = {}
    item['song_id'] = song_id
    item['song_name'] = song_name

    time.sleep(5)
    # print(driver.page_source)
    # page_source = driver.page_source
    # driver.find_element_by_id("srch").send_keys(u"炸山")
    # href = driver.find_element_by_xpath('')
    # print(href)

    driver.quit()
    song_load(item)

def song_load(item):
    song_id = item['song_id']
    song_name = item['song_name']

    song_url = 'https://music.163.com/song/media/outer/url?id={}'.format(song_id)
    #创建文件夹
    os.makedirs('wangyiyunmusic',exist_ok=True)
    path = 'wangyiyunmusic\{}.mp3'.format(song_name)
    #文本框
    text.insert(END,'歌曲: {}, 正在下载...').format(song_name)
    #文本框滚动
    text.see(END)
    #更新
    text.update()
    #下载
    urlretrieve(song_url,path)
    #文本框
    text.insert(END, '下载完毕: {}, 请试听...').format(song_name)
    # 文本框滚动
    text.see(END)
    #更新
    text.update()

if __name__ == '__main__':
    main()











