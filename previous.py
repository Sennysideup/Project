from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import time
from csv import reader
import pandas as pd
from html_table_parser import parser_functions
import collections
collections.Callable = collections.abc.Callable

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

url = ['####'] #선수 url 리스트

name=[]; count=0; player=[]; data=pd.DataFrame()

for urls in url:
    driver.get(urls)
    driver.implicitly_wait(10) #로딩이 끝날 때까지 10초까지 기다려줌
    driver.find_element(By.CSS_SELECTOR,"span.off").click() #기록 펼치기
    r=requests.get(urls)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser',from_encoding = 'utf-8')
    time.sleep(1)

    game_1 = soup.find('table',attrs={'class':'lst_board'}) #테이블 크롤링
    p=parser_functions.make2d(game_1) #여러 개의 열로 구분
    season=pd.DataFrame(p[1:]) #테이블 테이터 프레임화

    count=len(season) #데이터 프레임 행 개수 세기
    name_one = soup.find('p',attrs={'class':'name'}).text.strip() #선수 이름 크롤링
    name0=name_one+' ' #이름 사이에 공백 넣기
    name1=name0*count #선수 이름 반복
    name1=name1.split(' ') #공백 기준으로 문자열 나누기
    name1.pop() #마지막 공백 요소 삭제
    name.append(name1) #선수 이름 반복 리스트 만들기
    player=name.pop()

    data0=pd.DataFrame(p[1:], index=player, columns=['game','season','team','game_count','set_count','score','attack_percent','block_avg','serve_avg','set_avg','recive_eff','dig_avg','penalty','mistake'])
    data=data.append(data0)

data.to_csv('previous.csv', encoding='utf-8-sig', index=False)