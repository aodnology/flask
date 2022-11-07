from flask import Flask, render_template ,request
import urllib.request

#플라스크 인스턴스 초기화
app = Flask(__name__)

#라우트 데코레이터 사용하여 함수 실행
@app.route('/')

def index():
    return render_template('index.html')

@app.route("/newsview")
def spring():
    return render_template('index.html')
    
app.run(debug=True) 
# 기본적으로 5000포트에서 시작됨 변경시 run(port=5001) 식으로 변경
# debug=True : 내용 변경시 자동으로 플라스크가 이를 반영함
# 실제로 서비스할때는 사용 금지