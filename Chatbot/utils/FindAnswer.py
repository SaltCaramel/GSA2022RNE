from utils.CosineSimilarity import Similarity
from config.DatabaseConfig import *
import pymysql
# import pandas as pd

class FindAnswer:
    def __init__(self, query):
        # 질문/답변 학습 디비 연결 객체 생성
        self.query = query
        self.s = Similarity()

    def findAnswer(self, intent_name, query):
        db = None

        try:

            db = pymysql.connect(
                host=DB_HOST,
                user=DB_USER,
                passwd=DB_PASSWORD,
                db=DB_NAME,
                charset='utf8'
            )

            cond_name = intent_name
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
                querydb = qnadict["query"]
                answerdb = qnadict["answer"]
                x = self.s.findAns(sentence1=querydb, sentence2=query)
                #TEST CODE
                print("Query : " + querydb + ", ans :" + answerdb + ", Sim : " + str(x));
                if x > 0.5:
                    finquery = querydb
                    finans = answerdb
                    return finans
                elif maxsimquery <= x:
                    maxsimquery = x
                    finquery = querydb
                    finans = answerdb

            return finans

        except Exception as e:
            print(e)

        finally:
            if db is not None:
                db.close()


    # 답변 검색
    def search(self, intent_name, query):

        # 의도명, 개체명으로 답변 검색
        answer = self.findAnswer(intent_name, query)

        return (answer, None)

