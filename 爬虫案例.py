import urllib
import urllib.request


def loadPage(fullurl,filename):
        """
        作用是根据URL发总请求，获取服务器响应文件
        url：需要爬取的url地址
        filename:处理的文件名
        :return: 
        """
        print("正在下载" + filename )
        heards = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.36 Safari/537.36"}
        request = urllib.request.Request("url",headers = heards)
        return urllib.urlopen(request).read()

def writePage(html,filename):
        """
        作用：将html内容写入到本地
        HTML：服务器相应的文件内容
        :param html: 
        :return: 
        """
        print("正在保存" + filename)
        with open(filename,"w") as f:
            f.write(html)
        print("-"*30)
def tiebaSpider(url,beginPage,endPage):
    """
    作用：贴吧爬虫调度器，负责组合处理每个页面的url
    url：贴吧url的前半部分
    beginPage：起始页
    endPage：结束页
    :return: 
    """
    for page  in range(beginPage,endPage+1):
        pn = (page - 1)*50
        filename = "第" + str(page) + "页.html"
        fullurl = url +"&pn=" + str(pn)
        print(fullurl)
        html = loadPage(fullurl,filename)
        print(html)
        writePage(html,filename)
        print("谢谢使用")

if __name__ == "__main__":
    kw = input("请输入需要爬取的贴吧名")
    beginPage = int(input("请输入起始页： "))
    endPage = int(input("请输入结束页： "))
    url= r"htttp://tieba.baidu.com/f"
    key = urllib.parse.urlencode({"kw" : kw})
    fullurl = url + key
    tiebaSpider(fullurl,beginPage,endPage)
