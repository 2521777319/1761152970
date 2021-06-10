import jsonpath
import requests
import time
import pprint
class XM_Spider(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
        self.url = 'https://www.ximalaya.com/revision/album/v1/getTracksList?albumId=12576446&pageNum={}'
    def get_url_list(self):
        return [self.url.format(pn) for pn in range(1,18)]
    def parse(self,url):
        src_lst=[]
        title_lst=[]
        response = requests.get(url, headers=self.headers).json()
        pprint.pprint(response)
        titles = jsonpath.jsonpath(response, "$..'title'") #标题
        trackId = jsonpath.jsonpath(response, "$..'trackId'")#id

        for id_,title in zip(trackId,titles):
            video_url = 'https://www.ximalaya.com/revision/play/v1/audio?id={}&ptype=1'.format(id_)
            resp = requests.get(video_url,headers= self.headers).json()
            src = jsonpath.jsonpath(resp,"$..'src'")[0]
            src_lst.append(src)
            title_lst.append(title)
        return title_lst,src_lst

    def save(self,title_lst,src_lst):
        for title,src in zip(title_lst,src_lst):
            time.sleep(1)
            flv = requests.get(src,headers = self.headers).content
            with open(r'C:\Users\Administrator\Desktop\逻辑教育爬取文件\面向对象ximalaya\{}.m4a'.format(title),'wb')as f:
                f.write(flv)

    def main(self):
        url_list = self.get_url_list()
        for url in url_list:
            title_lst,src_lst=self.parse(url)
            self.save(title_lst,src_lst)
if __name__ == '__main__':
    xm = XM_Spider()
    xm.main()