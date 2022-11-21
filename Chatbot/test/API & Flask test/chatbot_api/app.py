from flask import Flask, request, jsonify, abort
import socket
import json
import time

from flask_cors import CORS


# 챗봇 엔진 서버 접속 정보
host = "127.0.0.1"  # 챗봇 엔진 서버 IP 주소
port = 5050  # 챗봇 엔진 서버 통신 포트

# Flask 어플리케이션
app = Flask(__name__)

CORS(app)
app.config['JSON_AS_ASCII'] = False




# 챗봇 엔진 서버와 통신
def get_answer_from_engine(bottype, query):
    # 챗봇 엔진 서버 연결
    mySocket = socket.socket()
    mySocket.connect((host, port))

    # 챗봇 엔진 질의 요청
    json_data = {
        'Query': query,
        'BotType': bottype
    }
    message = json.dumps(json_data)
    mySocket.send(message.encode())

    # 챗봇 엔진 답변 출력
    data = mySocket.recv(2048).decode()
    ret_data = json.loads(data)

    # 챗봇 엔진 서버 연결 소켓 닫기
    mySocket.close()

    return ret_data


@app.route('/', methods=['GET'])
def index():
    print('hello')


@app.route('/query/<query>', methods=['GET'])
def query(query):
    try:
        # 챗봇 API 테스트
        print("Connected")
        print('query', query)
        ret = get_answer_from_engine(bottype="TEST", query=query)
        print('ret', ret)
        return ret

    except Exception as ex:
        # 오류 발생시 500 오류
        abort(500)


laundry = 0
@app.route('/laundry', methods=['GET'])
def laundry():
    try:
        print("laundry has arrived")
        laundry = 1
        time.sleep(172800)
        laundry = 0

    except Exception as ex:
        # 오류 발생시 500 오류
        abort(500)

@app.route('/laundrycheck', methods=['GET'])
def laundryCheck():
    try:
        print("Client checked laundry")
        if laundry == 1:
            return 1
        else:
            return 0

    except Exception as ex:
        # 오류 발생시 500 오류
        abort(500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
