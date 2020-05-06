from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud

import os
import pandas as pd
import numpy as np
import re

import matplotlib.pyplot as plt
from PIL import Image                         # Pillow 패키지의 영상 핸들링 클래스.
import matplotlib 
from IPython.display import set_matplotlib_formats
import nltk 
from nltk.corpus import stopwords
%matplotlib qt 


os.chdir(r'C:\Users\연주\Desktop\career\청취아\final project\data\6. 네이버 지식인 워드클라우드 키워드 크롤링')
data = pd.read_excel("삼성카드_마일리지(완).xlsx")

okt = Okt()

nanum_data=[]  # word만 나옴
token_data=[]  # tag, word 모두 나옴
for line in data['content']:
    temp=okt.morphs(line, stem=True)
    nanum_data.append(temp)
    temp2=okt.pos(line, join=False)
    token_data.append(temp2)
    
# 불용어 Data가져오기
stop_words = pd.read_excel("korean_stop_words.xlsx")
stop_words = stop_words['불용어']
stop_words = list(stop_words)

# 본문에서 불용어 빼기
noun_list=[]

for sentence in token_data: 
    for word, tag in sentence : 
        if (tag in ['Noun']) and (word not in stop_words)and("삼성" not in word)and("카드" not in word)and("마일리지" not in word): 
            noun_list.append(word)

#단어 빈도
count = Counter(noun_list)
words = dict(count.most_common())


#TOP 10
import operator
top10=sorted(words.items(),key=operator.itemgetter(1), reverse=True)
top10[:20]

matplotlib.rc('font',family = 'Malgun Gothic') 
set_matplotlib_formats('retina')  # 폰트 선명하게
matplotlib.rc('axes',unicode_minus = False) # 그래프 음수 수치 오류 방지
#실행
wordcloud = WordCloud(background_color="black", font_path = 'C:/Windows/Fonts/malgun.ttf', colormap = "Set1", width=1500, height=1000).generate_from_frequencies(words) 
plt.imshow(wordcloud) 
plt.axis('off') 
plt.show()
