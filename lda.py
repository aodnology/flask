import pandas as pd
import konlpy
from wordcloud import WordCloud # 워드클라우드 생성
import PIL
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib
import os
import pickle
import datetime

# 오류 해소
matplotlib.use('TkAgg')

# 분석할 파일
json_file = input('토픽모델링할 기사제목 입력 : ')
time = datetime.datetime.now()

#데이터 불러오기
df = pd.read_json(("/Users/hayea/Documents/flask/Json_db/%s%s%s.json" %(time.month ,time.day, json_file)),encoding='UTF-8')

#불필요한 문자 제거
df['title'] = df['title'].str.replace('[^가-힣]|%s','' , regex = True)
kkma = konlpy.tag.Kkma()

# 명사 추출
nouns = df['title'].apply(kkma.nouns)
nouns = nouns.explode()

#데이터 프레임 생성
df_word = pd.DataFrame({'word' : nouns})
#글자수 추가
df_word['count'] = df_word['word'].str.len()
#두 글자 이상 단어만 남기기
df_word = df_word.query('count >= 2')
print(df_word)

#빈도표 만들기
df_word = df_word.groupby('word', as_index= False) \
    .agg(n = ('word', 'count')) \
        .sort_values('n', ascending=False)

#데이터 프레임 딕셔너리로 변환
dic_word = df_word.set_index('word').to_dict()['n']

# 파일 이름
time = datetime.datetime.now()
pkl_name = json_file
#텍스트 마이닝이 완료된 데이터 프레임 피클로 저장
with open('/Users/hayea/Documents/flask/pkl_object/%s%s%s.pkl' %(time.month ,time.day, pkl_name), 'wb') as f:
    pickle.dump(dic_word, f, pickle.HIGHEST_PROTOCOL)

# # 이미지 불러오기
# icon = PIL.Image.open('/Users/hayea/Documents/Python/cloud.png')

# # # mask 생성
# img = PIL.Image.new('RGB', icon.size,(255,255,255))
# img.paste(icon, icon)
# img = np.array(img)

# # 맥 폰트 오류
# rc('font', family='AppleGothic')
# plt.rcParams['axes.unicode_minus'] = False

# # wc 생성
# wc = WordCloud(
#     random_state= 1234,
#     font_path= 'AppleGothic',
#     width =400,
#     height= 400,
#     background_color= 'white'
#     # mask = img
# )
# #워드클라우드 만들기
# img_wordcloud = wc.generate_from_frequencies(dic_word)

# #워드 클라우드 출력하기
# plt.figure(figsize=(10, 10))
# plt.axis('off')
# plt.imshow(img_wordcloud)
# plt.show()
# plt.close()
