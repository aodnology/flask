import matplotlib.pyplot as plt
from matplotlib import rc
from wordcloud import WordCloud
import pickle
import datetime

key_word = input("워드클라우드로 보고싶은 종목을 입력하세요 : ")

time = datetime.datetime.now()

#피클 가져오기
with open('/Users/hayea/Documents/flask/pkl_object/%s%s%s.pkl' %(time.month ,time.day, key_word),'rb') as f:
    data = pickle.load(f)

# 맥 폰트 오류
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

# wc 생성
wc = WordCloud(
    random_state= 1234,
    font_path= 'AppleGothic',
    width =400,
    height= 400,
    background_color= 'white'
    # mask = img
)
#워드클라우드 만들기
img_wordcloud = wc.generate_from_frequencies(data)
time = datetime.datetime.now()

#워드 클라우드 출력하기
plt.figure(figsize=(5, 5))
plt.axis('off')
plt.imshow(img_wordcloud)

# plt.show(), plt.savefig() 둘다 사용하는 것은 불가능
# plt.show()
# 이미지를 불러올 경우를 대비해 이미지파일은 날짜 정보 입력 하지않음
plt.savefig(
    '/Users/hayea/Documents/flask/img/%s.png' %key_word,
    facecolor='#eeeeee',
    format='png'
    )
plt.close()