from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


@app.route('/api/result', methods=['POST'])
def answer():
    req = request.form['score']
    print(req)
    score = int(req)
    print(score)
    title = ''




    if score < 30:
        title = 'result_1.html'
    elif score < 50:
        title = 'result_2.html'
    elif score < 70:
        title = 'result_3.html'
    elif score < 90:
        title = 'result_4.html'
    elif score < 110:
        title = 'result_5.html'

    # else:
    #     title = 'result_2.html'
    return jsonify({'result': title})  # JSON 응답


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result_1.html')
def result_1():
    return render_template('result_1.html')

@app.route('/result_2.html')
def result_2():
    return render_template('result_2.html')

@app.route('/result_3.html')
def result_3():
    return render_template('result_3.html')

@app.route('/result_4.html')
def result_4():
    return render_template('result_4.html')

@app.route('/result_5.html')
def result_5():
    return render_template('result_5.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
