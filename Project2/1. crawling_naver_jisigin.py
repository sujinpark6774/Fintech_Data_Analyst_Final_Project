import os
from selenium import webdriver
import bs4,re
import pandas as pd
import numpy as np
import time

os.chdir(r'C:\Users\Gram\Desktop\myPyCode\project')

driver1 = webdriver.Chrome("./chromedriver")
search = '비씨카드'

driver1.get(" https://search.naver.com/search.naver?where=kin&query="+search+"&kin_sort=0&c_id=&c_name=&sm=tab_opt&sec=1&title=1&answer=0&grade=0&choice=0&nso=so%3Add%2Ca%3At%2Cp%3Afrom20190101to20191231&ie=utf8")
       
page=0
title=[]

while(True):
        
    html = driver1.page_source
    soup = bs4.BeautifulSoup(html, 'html.parser')
    
    if page == 1:
        page+=2
    else:
        page+=1
        
    
    title_test=driver1.find_elements_by_css_selector("li>dl>dt>a")
    for s in title_test:
        title.append(s.text)
    
    ## 페이지 넘기기 ## 수정주의!!
    # try except 사용하기 while문 추가하기
    try:
        driver1.find_element_by_css_selector("a.next").click()
    except:
        break
    
## title_Text 저장하기

news={"title":title}
df_news=pd.DataFrame(news,columns=['title'])

df_news.to_excel(search+".xlsx")
