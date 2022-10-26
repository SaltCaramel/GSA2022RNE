from config.DatabaseConfig import *
from utils.CosineSimilarity import Similarity
import pymysql

s = Similarity()

query = "광주과학고등학교는 어떤 학교인가요?"
db = None
try:
    # DB 호스트 정보에 맞게 입력해주세요
    db = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
        db=DB_NAME,
        charset='utf8'
    )

    # 이름 검색
    cond_name = '학교'
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = ''' 
        select * from chatbot_train_data where intent="%s"
        ''' % cond_name
        cursor.execute(sql)
        result = cursor.fetchall()

    maxsimquery = 0.0
    finquery = None
    finans = None

    for qnadict in result:
        print(qnadict["query"])
        querydb = qnadict["query"]
        answerdb = qnadict["answer"]
        x = s.findAns(sentence1=querydb, sentence2=query)
        print("similarity : " + str(x))
        print("=" * 100)
        if maxsimquery <= x:
            maxsimquery = x
            finquery = querydb
            finans = answerdb

    print("질문 : " + query)
    print("가장 유사한 질문: " + finquery)
    print("챗봇의 답변 : " + finans)



except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()



