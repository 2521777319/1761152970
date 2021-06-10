import requests
from fake_useragent import UserAgent
import json
from lxml import etree

url = 'https://haokan.baidu.com/videoui/api/videorec?tab=gaoxiao&act=pcFeed&pd=pc&num=20&shuaxin_id=1579074841838'
headers = {
    'User-Agent' : UserAgent().random
}

req = requests.get(url,headers = headers,timeout = 30).text
# print(req)
#json数据
#loads/load/dumps/dump/都是什么意思需要看看
data = json.loads(req)
#print(data)
""""

#字典的遍历（这些字典遍历什么的基础内容需要掌握）
#下面这种遍历方式就是层层遍历，在字典中以键值对的形式出现，
{'key':'value',{'key':'value'}}的形式出现，剥洋葱的方式进行层层遍历，
详情主要看json的内容，如本节的data内容，可以打印出来看一看就明白了。

"""
data_list = data['data']['response']['videos']
#print(data_list)
for info in data_list:
    title = info['title']
    video_url = info['play_url']
    source_name = info['source_name']
    print('正在下载：',title + 'mp4')
    video = requests.get(video_url,headers = headers,timeout = 30).content
    with open(r'D:\Users\asus\Desktop\video' + title + 'mp4' + source_name,'wb') as f:
        f.write(video)
        print('下载完成 ！\n')

#这里的json内容比较多，只下载了第一页的20个数据
#这里的json数据是动态加载的就是ajax的但是动态加载出来的url是一样的就看看滚动条的东西了