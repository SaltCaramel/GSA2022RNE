import socket
import json
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

# 챗봇 엔진 서버 접속 정보
host = "127.0.0.1"  # 챗봇 엔진 서버 IP 주소
port = 5050  # 챗봇 엔진 서버 통신 포트
"""
main = Blueprint('main', __name__, url_prefix='x')

@main.route('main', metiods = ['GET'])
def index():
    return render_template('index.html')

@main.route('main', metiods = ['GET'])
def every():
    return render_template('every.html')

@main.route('main', metiods = ['GET'])
def chatbot():
    return render_template('index.html')
"""
# 클라이언트 프로그램 시작
while True:
    print("질문 : ")
    query = input()  # 질문 입력
    if(query == "exit"):
        exit(0)
    print("-" * 40)

    # 챗봇 엔진 서버 연결
    mySocket = socket.socket()
    mySocket.connect((host, port))

    # 챗봇 엔진 질의 요청
    json_data = {
        'Query': query,
        'BotType': "MyService"
    }
    message = json.dumps(json_data)
    mySocket.send(message.encode())

    # 챗봇 엔진 답변 출력
    data = mySocket.recv(2048).decode()
    ret_data = json.loads(data)
    print("답변 : ")
    print(ret_data['Answer'])
    print(ret_data)
    print(type(ret_data))
    print("\n")

    # 챗봇 엔진 서버 연결 소켓 닫기
    mySocket.close()
