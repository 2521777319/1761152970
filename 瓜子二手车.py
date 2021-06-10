import requests
#这个库可能不能使用就像在这里只能使用浏览器的ua和cookie
from fake_useragent import UserAgent
from lxml import etree


headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
    'Cookie' : 'track_id=34703901822885888; uuid=2629df58-ece9-4953-e63a-a3fdd9590631; ganji_uuid=6882855039636021146609; lg=1; user_city_id=204; antipas=5096U326308Y78D2586245f5a; clueSourceCode=%2A%2300; preTime=%7B%22last%22%3A1579487571%2C%22this%22%3A1579429257%2C%22pre%22%3A1579429257%7D; sessionid=87169b44-d25c-4f9d-be73-8b27af7c8058; cityDomain=tj; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22pcbiaoti%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22%22%2C%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22ca_transid%22%3A%22%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22track_id%22%3A%2234703901822885888%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%222629df58-ece9-4953-e63a-a3fdd9590631%22%2C%22ca_city%22%3A%22zz%22%2C%22sessionid%22%3A%2287169b44-d25c-4f9d-be73-8b27af7c8058%22%7D; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A38096162879%7D'
}
# 获取汽车详情页面的url
def get_detail_urls():
    url = 'https://www.guazi.com/cs/buy/01/#bread'
    req =  requests.get(url,headers = headers,timeout = 30).content
    # print(req.decode('utf-8'))
    html = etree.HTML(req)
    ul = html.xpath('//ul [@class="carlist clearfix js-top"]')[0]
    lis = ul.xpath('./li')
    detail_urls = []
    for li in lis:
        detail_url = li.xpath('./a/@href')
        detail_url = 'https://www.guazi.com/' + detail_url[0]
        detail_urls.append(detail_url)
        #print(detail_url)
    return detail_urls

#提取详情页面的数据
def parse_detail_page(url):
    resp = requests.get(url,headers = headers,timeout = 30).text
    html = etree.HTML(resp)
    title = html.xpath('//div[@class="product-textbox"]/h2/text()')
    info = html.xpath('//div[@class="product-textbox"]/ul/li/span/text()')
    infos = {}
    cardtime = info[0]
    km = info[1]
    displacement = info[2]
    speedbox = info[3]
    infos['title'] = title
    infos['cardtime'] = cardtime
    infos['km'] = km
    infos['displacement'] = displacement
    infos['speedbox'] = speedbox
    return infos

def main():
    detail_urls = get_detail_urls()
    for detail_url in detail_urls:
        infos = parse_detail_page(detail_url)
        print(infos)
if __name__ == '__main__':
    main()




