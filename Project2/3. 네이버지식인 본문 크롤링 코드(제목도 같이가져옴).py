import os
from selenium import webdriver
import bs4,re
import pandas as pd
import numpy as np
import time


os.chdir(r'C:\Users\Gram\Desktop\네이버지식인')
#######################################
############### 불러올 파일 이름 입력
search='국민카드설계사'
save_name="국민카드설계사_본문"
# 화면 2
driver2 = webdriver.Chrome("./chromedriver")
re_excel=pd.read_excel(search+".xlsx")

title=[]
content=[]
for link in re_excel['link']:
    driver2.get(link)
    
    # 제목저장
    driver2.find_elements_by_css_selector("div#content")
    subject=driver2.find_element_by_css_selector("div.question-content>div>div>div>div>div.title")
    title.append(subject.text)
    time.sleep(1)
    ##
    try:
        subject=driver2.find_element_by_css_selector("div.question-content>div>div>div.c-heading__content")
        content.append(subject.text)
    except:
        content.append('')


#중복제거 코드
re_data = []
for i in range(len(title)):
    re_data.append((title[i],content[i]))

re_data=set(re_data)

df_data=pd.DataFrame(re_data,columns=['title','content'])

save_doc={"title":df_data['title'],"content":df_data['content']}
df_news=pd.DataFrame(save_doc,columns=["title","content"])
df_news.to_excel(save_name+".xlsx")


