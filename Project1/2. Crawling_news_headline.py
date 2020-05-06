# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 11:47:43 2020

@author: Owner
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 19:08:13 2020

@author: Owner
"""
import os
from selenium import webdriver
import bs4,re
import pandas as pd
import numpy as np
import time

os.chdir(r'C:\workspace\Python\4-2) 핀테크 교육\Final Project\Project1')

driver1 = webdriver.Chrome("./chromedriver")

# 검색 키워드
search_list = ['패션']

# 화면1
for search in search_list:
    driver1.get("https://search.naver.com/search.naver?where=news&query="+search+"&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=2017.11.01&de=2018.05.31&docid=&nso=so%3Ar%2Cp%3Afrom20171101to20180531%2Ca%3Aall&mynews=0&refresh_start=0&related=0")

    title=[]
    contents=[]
    while(True):

        # title, contents
        driver1.find_elements_by_css_selector("ul.type01")
        title_content = driver1.find_elements_by_css_selector("dl>dt>a")
        contents_list = driver1.find_elements_by_xpath("//*/dl/dd[2]")

        for t in range(len(title_content)):
            if (title_content[t].text == '도움말') & (contents_list[t].text == ''):
                continue
            else:
                title.append(title_content[t].text)
                ob = contents_list[t].text
                ob = ob.replace("=", "")
                contents.append(ob)

        try:
            driver1.find_element_by_css_selector("a.next").click()
        except:
            break

    news={"title":title, "contents":contents}

    df_news=pd.DataFrame(news, columns=['title','contents'])
    
    df_news.to_excel(search+".xlsx")
