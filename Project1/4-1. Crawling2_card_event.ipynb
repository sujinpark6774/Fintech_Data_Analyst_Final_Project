# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import bs4
from selenium import webdriver
import os
import time

#신한카드
os.getcwd()
os.chdir(r'C:\anaconda')
my_driver = webdriver.Chrome('chromedriver.exe') 
my_driver.get("https://www.shinhancard.com/conts/person/event/event/last_event.jsp")


test=[]

while (True):
    my_driver.find_element_by_xpath("//*[@id='pE-ListmoreJo']/div[1]").click()
    time.sleep(3)
#break 수동으로 해결

res = my_driver.find_elements_by_css_selector('td.textL')
for x in res:
    #print(x.text)
    test.append(x.text)
    
del test[1098:]
sh = pd.DataFrame(data=test)
sh.to_csv('sh_name.csv')

sh_date=[]
for page in range(1,1099):
    date=my_driver.find_element_by_xpath("//*[@id='pE-ListmoreJo']/table/tbody/tr["+str(page)+"]/td[2]")
    sh_date.append(date.text)

col_names=['context','date']
sh2 = pd.DataFrame(data=sh_date)

sh_total = pd.concat([sh,sh2],axis=1,names=['context','date'])
sh_total.to_csv('sh_total.csv', encoding='cp949')


#하나카드
os.chdir(r'C:\Users\연주\Desktop\career\청취아\파이널 프로젝트\data')

hana_driver = webdriver.Chrome('chromedriver.exe')
hana_driver.get("https://www.hanacard.co.kr/OPP35050000D.web?schID=pcd&mID=OPP35050000D")


hn_text=[]
hn_date=[]
while(True):        
    html = hana_driver.page_source
    soup = bs4.BeautifulSoup(html, 'html.parser')
    
    tags = hana_driver.find_elements_by_css_selector('td.left')
    for atag in tags:
        hn_text.append(atag.text)
    for i in range(1,11): 
        hana_date = hana_driver.find_element_by_xpath("//*[@id='container']/div/div/div/article[1]/div[1]/table/tbody/tr["+str(i)+"]/td[2]")
        hn_date.append(hana_date.text)
    
    try:
        hana_driver.find_element_by_xpath("//*[@id='container']/div/div/div/article[1]/div[2]/div[3]/a").click()
    except:
        break
    
hn = pd.DataFrame(data=hn_text, columns=['text'])
hn2 = pd.DataFrame(data=hn_date, columns=['date'])
hn_total = pd.concat([hn,hn2],axis=1,names=['context','date'])
hn_total.to_csv('hn_total.csv', encoding='cp949')
    
#93페이지 까지는 그냥 넘기기
os.chdir(r'C:\Users\연주\Desktop\career\청취아\파이널 프로젝트\data')

hana_driver = webdriver.Chrome('chromedriver.exe')
hana_driver.get("https://www.hanacard.co.kr/OPP35050000D.web?schID=pcd&mID=OPP35050000D")


hn_text=[]
hn_date=[]
page=1
while(True):   
    if (page <=93)&(page%10==1):
        page+=1
        hana_driver.find_element_by_xpath("//*[@id='container']/div/div/div/article[1]/div[2]/ul/li["+str(page)+"]/a").click()
    
    elif (page <=93)&(page%10==0):
        hana_driver.find_element_by_xpath("//*[@id='container']/div/div/div/article[1]/div[2]/div[3]/a").click()
    
    else :
     
        html = hana_driver.page_source
        soup = bs4.BeautifulSoup(html, 'html.parser')
        
        tags = hana_driver.find_elements_by_css_selector('td.left')
        for atag in tags:
            hn_text.append(atag.text)
             
            hana_date = hana_driver.find_element_by_xpath("//*[@id='container']/div/div/div/article[1]/div[1]/table/tbody/tr["+str(atag)+"]/td[2]")
            hn_date.append(hana_date.text)
        
        try:
            hana_driver.find_element_by_xpath("//*[@id='container']/div/div/div/article[1]/div[2]/div[3]/a").click()
        except:
            break


