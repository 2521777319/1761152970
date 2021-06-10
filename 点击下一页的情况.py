import requests
import time
from fake_useragent import UserAgent
from random import randint

class get_main_html():
    def __init__(self):
        self.url = ''
        self.next_url = []