from config.DatabaseConfig import *
from utils.Database import Database
from utils.Preprocess import Preprocess



# 전처리 객체 생성
p = Preprocess(word2index_dic='../train_tools/dict/chatbot_dict.bin'
               ,userdic='../utils/user_dic.tsv')

# 질문/답변 학습 디비 연결 객체 생성
db = Database(
    host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db_name=DB_NAME
)
db.connect()    # 디비 연결

query = "광주과학고등학교는 어떤 학교인가요?"

# 의도 파악
from models.intent.IntentModel import IntentModel
intent = IntentModel(model_name='../models/intent/intent_model.h5', proprocess=p)
predict = intent.predict_class(query)
intent_name = intent.labels[predict]

# 개체명 인식
from models.ner.NerModel import NerModel
ner = NerModel(model_name='../models/ner/ner_model.h5', proprocess=p)
predicts = ner.predict(query)
ner_tags = ner.predict_tags(query)

print("질문 : ", query)
print("=" * 100)
print("의도 파악 : ", intent_name)
print("=" * 100)

# 답변 검색
from utils.FindAnswer import FindAnswer

try:
    if intent_name == "욕설":
        answer = "욕하지 마세요 ㅠㅠ"

    elif intent_name == "기타":
        answer = "죄송해요. 무슨 말인지 모르겠어요. 조금 더 공부 할게요."

    else:
        f = FindAnswer(db)
        answer, answer_image = f.search(intent_name, query)
except:
    answer = "죄송해요 무슨 말인지 모르겠어요"

print("답변 : ", answer)

db.close() # 디비 연결 끊음