#-*- coding: utf-8 -*-
import requests
from fake_useragent import UserAgent
from lxml import etree
import time
import re
#网易云音乐外链地址：https://music.163.com/song/media/outer/url?id=
#外链网站：https://link.hhtjim.com/



headers = {
    'User-Agent' : UserAgent().random
}
#https://music.163.com/discover/toplist?id=19723756
# url = 'https://m10.music.126.net/20200205143429/be6241062ab9e842b2352da28178200e/yyaac/030b/015b/5652/4a503d3c0461ab191be8a8b7ceb87598.m4a'
base_url = 'https://music.163.com/discover/toplist'
req = requests.get(base_url,headers = headers,timeout = 30)
req.encoding = 'utf-8'
req = req.text
time.sleep(5)
title = re.findall('<img .*? alt="(.*?)"/>',req)
# print(title)
# print(req)
id = re.findall('<a class="avatar" href="(.*?)">',req)
# print(id)
for id,title in zip(id,title):
    url = 'https://music.163.com' + id
    # print(url,title)
    htmls = requests.get(url,headers = headers,timeout = 30)
    htmls.encoding = 'utf-8'
    htmls = htmls.text
    time.sleep(5)
    # print(htmls)
    # print('==============================')
    ul = re.findall(r'<ul class="f-hide">.*?</ul>',htmls,re.S)[0]
    song_list = re.findall(r'id=(.*?)">(.*?)</a></li>', ul)
    # print(song_list)
    for song_info in song_list:
        song_id, song_name = song_info
        # print(song_name)
        # print(song_id)
        #https://link.hhtjim.com/163/1303289043.mp3
        song_url = 'https://link.hhtjim.com/163/' + '%s' % song_id + '.mp3'
        # print(song_url)
        music = requests.get(song_url,headers = headers,timeout = 30).content
        with open('D:\音乐\%s.m4a'%song_name,'wb') as f:
            f.write(music)
            print('%s'%song_name + '已经下载完毕')

    # print(songs_all)
