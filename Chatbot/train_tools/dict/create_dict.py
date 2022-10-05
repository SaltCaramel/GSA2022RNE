# 챗봇에서 사용하는 사전 파일 생성
# 왜 파이참에서 안되는지는 모르겠다만 코랩에서 학습해놓은게 있으니까 그거로 쓸개오

# 2022.09.05 파일 업데이트 : 광주과학고 나무위키, 공식 사이트 등 학습
# 2022.09.06 파일 업데이트 : 광곽, 팡팍 학습 .. 실패

from utils.Preprocess import Preprocess
from tensorflow import keras
from keras import preprocessing
import pickle

# 말뭉치 데이터 읽어오기
def read_corpus_data(filename):
    with open(filename, 'r', 'utf-8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]
    return data


# 말뭉치 데이터 가져오기
corpus_data = read_corpus_data('./corpus.txt')


# 망뭉치 데이터에서 키워드만 추출해서 사전 리스트 생성
p = Preprocess(word2index_dic='chatbot_dict.bin',
               userdic='../../utils/user_dic.tsv')
dict = []
for c in corpus_data:
    pos = p.pos(c[1])
    for k in pos:
        dict.append(k[0])
    # keywords = p.get_keywords(pos, without_tag=True)
    # for k in keywords:
    #     dict.append(k)

# 사전에 사용될 word2index 생성
# 사전의 첫번 째 인덱스에는 OOV 사용
tokenizer = preprocessing.text.Tokenizer(oov_token='OOV')
tokenizer.fit_on_texts(dict)
word_index = int(tokenizer.word_index)

# 사전 파일 생성
f = open("chatbot_dict.bin", "wb")
try:
    pickle.dump(int(word_index), f)
except Exception as e:
    print(e)
finally:
    f.close()
