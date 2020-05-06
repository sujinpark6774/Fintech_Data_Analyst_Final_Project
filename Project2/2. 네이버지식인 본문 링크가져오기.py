import os
from selenium import webdriver
import bs4,re
import pandas as pd
import numpy as np
import time


os.chdir(r'C:\Users\Gram\Desktop\네이버지식인')


###############
    
# 화면1
driver1 = webdriver.Chrome("./chromedriver")
search='국민카드설계사'

# 날짜 변경
driver1.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=kin&query="+search+"&oquery="+search+"&tqi=UC5uqlprvxsssFFpvRossssstuG-126871&nso=so%3Add%2Ca%3At%2Cp%3Afrom20190101to20191231&answer=0&choice=0&grade=0&kin_sort=0&sec=1&title=1")

link_list=[]
while(True):
    subject=driver1.find_elements_by_css_selector("ul#elThumbnailResultArea>li>dl>dt>a")
    for s in subject:
        link_list.append(s.get_attribute('href'))
        
    try:
        driver1.find_element_by_css_selector("a.next").click()
    except:
        break

test={"link":link_list}
df_news=pd.DataFrame(test,columns=["link"])
df_news.to_excel(search+".xlsx")



