from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


url = ['####'] #선수 url 리스트
name = []
attack1 = []; attack2 = []; attack3=[]; attack4=[]; attack5=[]; attack6=[]
block1 = []; block2 = []; block3=[]; block4=[]; block5=[]; block6=[]; block7=[]
serve1 = []; serve2 = []; serve3=[]; serve4=[]; serve5=[]
set1 = []; set2 = []; set3=[]; set4=[]; set5=[]
recive1 = []; recive2 = []; recive3=[]; recive4=[]; recive5=[]
dig1 = []; dig2 = []; dig3=[]; dig4=[]; dig5=[]

for urls in url:
    driver.get(urls)
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR,"span.off").click() #기록 펼치기
    r=requests.get(urls)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser',from_encoding = 'utf-8')
    time.sleep(1)

    name_one = soup.find('p',attrs={'class':'name'}).text.strip()
    name.append(name_one)

    attack_try = soup.select_one('#detail1 > div.record.type1.clearfix > dl:nth-child(1) > dd').text.rstrip()
    attack1.append(attack_try)
    attack_success = soup.select_one('#detail1 > div.record.type1.clearfix > dl:nth-child(2) > dd').text.rstrip()
    attack2.append(attack_success)
    attack_mistake = soup.select_one('#detail1 > div.record.type1.clearfix > dl:nth-child(3) > dd').text.rstrip()
    attack3.append(attack_mistake)
    attack_block = soup.select_one('#detail1 > div.record.type1.clearfix > dl:nth-child(4) > dd').text.rstrip()
    attack4.append(attack_block)
    attack_success_rate = soup.select_one('#detail1 > div.record.type1.clearfix > dl:nth-child(5) > dd').text.rstrip()
    attack5.append(attack_success)
    attack_possession = soup.select_one('#detail1 > div.record.type1.clearfix > dl:nth-child(6) > dd').text.rstrip()
    attack6.append(attack_possession)

    block_try = soup.select_one('#detail2 > div.record.type2.clearfix > dl:nth-child(1) > dd').text.rstrip()
    block1.append(block_try)
    block_success = soup.select_one('#detail2 > div.record.type2.clearfix > dl:nth-child(2) > dd').text.rstrip()
    block2.append(block_success)
    block = soup.select_one('#detail2 > div.record.type2.clearfix > dl:nth-child(3) > dd').text.rstrip()
    block3.append(block)
    block_fail = soup.select_one('#detail2 > div.record.type2.clearfix > dl:nth-child(4) > dd').text.rstrip()
    block4.append(block_fail)
    block_mistake = soup.select_one('#detail2 > div.record.type2.clearfix > dl:nth-child(5) > dd').text.rstrip()
    block5.append(block_mistake)
    block_count = soup.select_one('#detail2 > div.record.type2.clearfix > dl:nth-child(6) > dd').text.rstrip()
    block6.append(block_count)
    block_possession = soup.select_one('#detail2 > div.record.type2.clearfix > dl:nth-child(7) > dd').text.rstrip()
    block7.append(block_possession)

    serve_try = soup.select_one('#detail3 > div.record.type1.clearfix > dl:nth-child(1) > dd').text.rstrip()
    serve1.append(serve_try)
    serve_success = soup.select_one('#detail3 > div.record.type1.clearfix > dl:nth-child(2) > dd').text.rstrip()
    serve2.append(serve_success)
    serve_mistake = soup.select_one('#detail3 > div.record.type1.clearfix > dl:nth-child(3) > dd').text.rstrip()
    serve3.append(serve_mistake)
    serve_count = soup.select_one('#detail3 > div.record.type1.clearfix > dl:nth-child(4) > dd').text.rstrip()
    serve4.append(serve_count)
    serve_possession = soup.select_one('#detail3 > div.record.type1.clearfix > dl:nth-child(5) > dd').text.rstrip()
    serve5.append(serve_possession)

    set_try = soup.select_one('#detail4 > div.record.type1.clearfix > dl:nth-child(1) > dd').text.rstrip()
    set1.append(set_try)
    set_success = soup.select_one('#detail4 > div.record.type1.clearfix > dl:nth-child(2) > dd').text.rstrip()
    set2.append(set_success)
    set_mistake = soup.select_one('#detail4 > div.record.type1.clearfix > dl:nth-child(3) > dd').text.rstrip()
    set3.append(set_mistake)
    set_count = soup.select_one('#detail4 > div.record.type1.clearfix > dl:nth-child(4) > dd').text.rstrip()
    set4.append(set_count)
    set_possession = soup.select_one('#detail4 > div.record.type1.clearfix > dl:nth-child(5) > dd').text.rstrip()
    set5.append(set_possession)

    recive_try = soup.select_one('#detail5 > div.record.type1.clearfix > dl:nth-child(1) > dd').text.rstrip()
    recive1.append(recive_try)
    recive_success = soup.select_one('#detail5 > div.record.type1.clearfix > dl:nth-child(2) > dd').text.rstrip()
    recive2.append(recive_success)
    recive_mistake = soup.select_one('#detail5 > div.record.type1.clearfix > dl:nth-child(3) > dd').text.rstrip()
    recive3.append(recive_mistake)
    recive_eff = soup.select_one('#detail5 > div.record.type1.clearfix > dl:nth-child(4) > dd').text.rstrip()
    recive4.append(recive_eff)
    recive_possession = soup.select_one('#detail5 > div.record.type1.clearfix > dl:nth-child(5) > dd').text.rstrip()
    recive5.append(recive_possession)

    dig_try = soup.select_one('#detail6 > div.record.type1.clearfix > dl:nth-child(1) > dd').text.rstrip()
    dig1.append(dig_try)
    dig_success = soup.select_one('#detail6 > div.record.type1.clearfix > dl:nth-child(2) > dd').text.rstrip()
    dig2.append(dig_success)
    dig_mistake = soup.select_one('#detail6 > div.record.type1.clearfix > dl:nth-child(3) > dd').text.rstrip()
    dig3.append(dig_mistake)
    dig_count = soup.select_one('#detail6 > div.record.type1.clearfix > dl:nth-child(4) > dd').text.rstrip()
    dig4.append(dig_count)
    dig_possession = soup.select_one('#detail6 > div.record.type1.clearfix > dl:nth-child(5) > dd').text.rstrip()
    dig5.append(dig_possession)

    time.sleep(1)

    current = pd.DataFrame(zip(name,attack1, attack2, attack3,attack4, attack5, attack6,
    block1, block2, block3, block4, block5, block6, block7,
    serve1, serve2, serve3,serve4, serve5,
    set1, set2, set3, set4, set5,
    recive1, recive2, recive3, recive4, recive5,
    dig1, dig2, dig3, dig4, dig5),columns=['이름','공격 시도','공격 성공','공격 범실','상대 블록','공격 성공률', '공격 점유율',
    '블로킹 시도', '블로킹 성공', '유효 블로킹', '블로킹 실패', '블로킹 범실', '블로킹 개수', '블로킹 점유율',
    '서브 시도', '서브 성공', '서브 범실', '서브 개수', '서브 점유율',
    '세트 시도', '세트 성공', '세트 범실', '세트 개수', '세트 점유율',
    '리시브 시도', '리시브 정확', '리시브 실패', '리시브 효율', '리시브 점유율',
    '디그 시도', '디그 정확', '디그 실패', '디그 개수', '디그 점유율'])

current.to_csv('recent.csv', encoding='utf-8-sig', index=False)