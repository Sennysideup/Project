from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

import requests
from bs4 import BeautifulSoup
import time
from csv import reader
import pandas as pd
from html_table_parser import parser_functions
import collections
collections.Callable = collections.abc.Callable
import urllib.request; import ssl; import dload

url = ['####'] #선수 url 리스트
base = 'https://www.kovo.co.kr'

for urls in url:
    driver.get(urls)
    driver.implicitly_wait(10) #로딩이 끝날 때까지 10초까지 기다려줌
    driver.find_element(By.CSS_SELECTOR,"span.off").click() #기록 펼치기
    r=requests.get(urls)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser',from_encoding = 'utf-8')
    time.sleep(1)

    name_one = soup.find('p',attrs={'class':'name'}).text.strip() #선수 이름 크롤링
    name=str(name_one)
    img = soup.find('div',attrs={'class':'img'}) #선수 프로필 사진 크롤링
    imgUrl = soup.select('#tab2 > div.player_profile.box > div > div.img > img')

    for images in imgUrl:
        src = images['src']
        print(src)
        imageurl = base+src
        print(imageurl)
        dload.save(imageurl,f'{name}.jpg')
    time.sleep(1)