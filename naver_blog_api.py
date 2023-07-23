#-*- coding: utf-8 -*-

import os
import sys
import urllib.request
import re
import pandas as pd
import time
from bs4 import BeautifulSoup
import numpy as np
import requests

class naver_blog:
    def __init__(self, client_id, client_secret, search, num, start):
        self.client_id = client_id
        self.client_secret = client_secret
        self.search = search
        self.num = num
        self.start = start

    def blog_api(self): #search : 검색어, num : 출력할 개수
        encText = urllib.parse.quote(self.search)
        url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=" + str(self.num) + "&start=" + str(self.start) # json
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", self.client_id)
        request.add_header("X-Naver-Client-Secret", self.client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()

        if(rescode==200):
            response_body = response.read()
            body = response_body.decode('utf-8')
            return body
        else:
            print("Error Code:" + rescode)

    def preprocessing(self, body): #전처리
        body = body.replace('"','')
        list1 = body.split('\n\t\t{\n\t\t\t')
        list1 = [i for i in list1 if 'naver' in i]

        titles = list(); links = list(); dates = list()
        for i in list1: #제목, 링크, 날짜
            title = i.split("\n\t\t\t")[0]
            title = title.replace('title:',"")
            link = i.split("\n\t\t\t")[1]
            link = link.replace('link:',"")
            postdate = i.split("\n\t\t\t")[-1]
            postdate = re.sub(r'[^0-9]',"", postdate) #숫자만 남기기
            titles.append(title)
            links.append(link)
            dates.append(postdate)

        for i in range(len(titles)): #전처리
            titles[i] = titles[i].replace("<\/b>", "")
            titles[i] = titles[i].replace("<b>", "")
            titles[i] = titles[i].replace(",", "")
            links[i] = links[i].replace("\\",'')
            links[i] = links[i].replace(",", "")
            
        # 제목, 링크, 날짜 데이터프레임 만들기
        df = pd.DataFrame({"title":titles, "link":links, "postdate":dates, "text":np.nan})
        return df