from multiprocessing import Pool
import requests
import re
import json

def main(page):
    page = page + 10
    url = 'https://maoyan.com/board/4?offset=' + str(page)
    print(url)

if __name__ == '__main__':

    #创建进程
    pool = Pool(5)
    pool.map(main,[i * 10 for i in range(10)])