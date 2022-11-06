import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib
from wordcloud import WordCloud
import pickle

key_word = input("워드클라우드로 보고싶은 종목을 입력하세요 : ")

#피클 가져오기
with open('/Users/hayea/Documents/flask/pkl_object/%s.pkl'%key_word,'rb') as f:
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

#워드 클라우드 출력하기
plt.figure(figsize=(10, 10))
plt.axis('off')
plt.imshow(img_wordcloud)
plt.show()
plt.close()