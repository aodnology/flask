import sqlite3

# sql 데이터베이스 파일 연결
conn = sqlite3.connect('reviews.sqlite')
# cursor() 데이터베이스 커서생성
c = conn.cursor()

# execute() 데이터베이스 테이블(review_db), 컬럼(review, sentiment, date) 생성
c.execute('CREATE TABLE review_db'\
    '(review TEXT, sentiment INTEGER, date TEXT)')

exam1 = '링크 차트 앱 참 괜찮네요'
c.execute("INSERT INTO review_db"\
    "(review, sentiment, date) VALUES" \
    "(?,?,DATETIME('now'))"), (exam1, 1)

exam2 = '링크 차트 앱 참 별로네요'
c.execute("INSERT INTO review_db"\
    "(review, sentiment, date) VALUES" \
    "(?,?,DATETIME('now'))"), (exam1, 0)

conn.commit()
conn.close()