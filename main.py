from flask import Flask, render_template
app = Flask(__name__)

# 크롤링 라이브러리 import
import requests
from bs4 import BeautifulSoup

@app.route('/')
def hello():

    req = requests.get("https://www.daum.net/")
    #req에 인자로 준 페이지의 html 코드를 soup로 담는다
    soup = BeautifulSoup(req.text, 'html.parser')
    #print(soup)

    #크롤링하고싶은 요소에서 "검사"를 눌러서 html 코드를 본다.
    #인기 검색어의 경우, li 태그의 a 태그 안에 담겨 있음
    #copy > copy selector 로 복사 가능

    list_daum = []
    #li의 모든 요소들을 list_daum 변수에 추가, 하나씩 출력
    for i in soup.select("#gnbServiceList > ul > li"):
        list_daum.append(i.find("a").text) #a 태그에서 text만 뽑아낸다

    return render_template("index.html", daum = list_daum)

@app.route('/about')
def about():
    return "여기는 어바웃페이지입니다."

if __name__ == '__main__':
    app.run()