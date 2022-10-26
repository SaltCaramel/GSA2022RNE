from flask import Flask, request, jsonify, abort
import socket
import json
<<<<<<< HEAD
from flask_cors import CORS
=======
>>>>>>> 618cddf0841d40e362b19244f4a59334ffad6d7c

# 챗봇 엔진 서버 접속 정보
host = "127.0.0.1"  # 챗봇 엔진 서버 IP 주소
port = 5050  # 챗봇 엔진 서버 통신 포트

# Flask 어플리케이션
app = Flask(__name__)
<<<<<<< HEAD
CORS(app)
app.config['JSON_AS_ASCII'] = False
=======
>>>>>>> 618cddf0841d40e362b19244f4a59334ffad6d7c


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

<<<<<<< HEAD

@app.route('/query/<query>', methods=['GET'])
def query(query):
    try:
        # 챗봇 API 테스트
        print("Connected");
        print('query', query)
        ret = get_answer_from_engine(bottype="TEST", query=query)
        print('ret', ret)
        return ret

    except Exception as ex:
        # 오류 발생시 500 오류
        abort(500)


"""
=======
>>>>>>> 618cddf0841d40e362b19244f4a59334ffad6d7c
# 챗봇 엔진 query 전송 API
@app.route('/query/<bot_type>', methods=['POST'])
def query(bot_type):
    body = request.get_json()

    try:
        if bot_type == "TEST":
            # 챗봇 API 테스트
<<<<<<< HEAD
            print("Connected");
=======
>>>>>>> 618cddf0841d40e362b19244f4a59334ffad6d7c
            ret = get_answer_from_engine(bottype=bot_type, query=body['query'])
            return jsonify(ret)

        elif bot_type == "KAKAO":
            # 카카오톡 스킬 처리
            pass

<<<<<<< HEAD
=======
        elif bot_type == "NAVER":
            # 네이버톡톡 Web hook 처리
            pass
>>>>>>> 618cddf0841d40e362b19244f4a59334ffad6d7c
        else:
            # 정의되지 않은 bot type인 경우 404 오류
            abort(404)

    except Exception as ex:
        # 오류 발생시 500 오류
        abort(500)
<<<<<<< HEAD
"""
=======

>>>>>>> 618cddf0841d40e362b19244f4a59334ffad6d7c

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
