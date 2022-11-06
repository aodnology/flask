from flask import Flask
import pandas as pd
import konlpy
from word_cloud import WordCloud # 워드클라우드 생성
import PIL
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib

app = Flask(__name__)

@app.route('/')
def index():
    
    return 'hi'

@app.route('/create/')
def create():
    return 'Create'

@app.route('/read/<id>/')
def read(id):
    print(id)
    return 'read ' +id

app.run(debug=True) 
# 기본적으로 5000포트에서 시작됨 변경시 run(port=5001) 식으로 변경

# debug=True : 내용 변경시 자동으로 플라스크가 이를 반영함
# 실제로 서비스할때는 사용 금지