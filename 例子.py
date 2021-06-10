import requests
from bs4 import BeautifulSoup
import wordcloud
import jieba

class Download(object):

    #定义初始化变量以及相关内容
    def __init__(self):
        self.target = 'http://www.quanshuwang.com/book/9/9055'
        self.href_list = []
        self.chapter_name = []
        self.num = 0
        self.head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
            'Accept': 'text/html,application/xhtml',
            'connection': 'keep-alive',
            'Accept - Encoding':'gzip, deflate'
            }

    #用于获取小说目录的全部url
    def get_url(self):
        req = requests.get(url=self.target,params='html',headers=self.head)
        req.encoding = 'gbk'
        html = req.text
        bf_url = BeautifulSoup(html,features="html.parser")
        div = bf_url.find_all('div',class_='clearfix')
        div_a = BeautifulSoup(str(div[1]),features="html.parser")
        a = div_a.find_all('a')
        #删除不要的章节！
        self.num = len(a[:10])
        #print(self.num)
        #print(a[:10])
        for each in a[:10]:
            self.chapter_name.append(each.string)
            self.href_list.append(each.get('href'))

    # URL获取好列表了，该模块进行下载储存
    def down_novel(self,herf):
        url = requests.get(url=herf)
        url.encoding='gbk'
        url_text = url.text
        url_bf = BeautifulSoup(url_text,features="html.parser")
        url_bf_div =url_bf.find_all('div',class_='mainContenr')
        self.url_bf_div_text= url_bf_div[0].text.replace('\xa0'*8,'\n\n')

    def write(self):
        with open('novel.txt', 'a', encoding='utf-8') as f:
            f.write('\n')
            f.writelines(self.url_bf_div_text)
            f.write('\n\n')

    def wordCloud_show(self):
        f = open('C:/Users/Administrator/PycharmProjects/practice2/novel.txt','r',encoding='utf-8')
        t = f.read()
        f.close()
        ls = jieba.lcut(t)
        txt = ' '.join(ls)
        w = wordcloud.WordCloud(font_path = 'c:\windows\Fonts\STZHONGS.TTF',width = 1000,height = 700,background_color = 'white')
        w.generate(txt)
        w.to_file('novelWordcloud.png')

if __name__ == '__main__':
    dl = Download()
    dl.get_url()
    index = 0
    for i in dl.href_list:
        dl.down_novel(i)
        dl.write()
        index += 1
        print("\r# Process: %0.2f %%" % (float(index) / float(dl.num)*100 ), end='')
    dl.wordCloud_show()
