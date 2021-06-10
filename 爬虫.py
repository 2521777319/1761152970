import urllib.request
import chardet   #第三方库chardet自动获取目标网页的编码

if __name__ == "__main__":

    ub_header = {
        "User-Agent": r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.36 Safari/537.36"
    } #伪装，防止网站的反爬机制认出需要添加header

    # 发送
    request = urllib.request.Request("http://baidu.com/",headers = ub_header)

    # 返回打开的网页信息
    response = urllib.request.urlopen(request)

    # 读取
    html = response.read()

    # 对返回的数据进行解码decode，才能显示正确的字符串
    html = html.decode("utf-8")

    # 返回HTTP的响应码，成功返回200,4服务器页面出错，5为服务器问题
    print(response.getcode())
    print(html)#打印

    # 返回实际数据的URL，防止重定向
    print(response.geturl())
    # 返回HTTP响应时的报头
    print(response.info())