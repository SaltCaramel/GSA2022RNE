from utils.Preprocess import Preprocess
from tensorflow import keras
from keras import preprocessing

sent = "광주과학고등학교는 뭐하는 곳이야?"
p = Preprocess(word2index_dic='../train_tools/dict/chatbot_dict.bin',
               userdic = '../utils/user_dic.tsv')

pos = p.pos(sent)
keywords = p.get_keywords(pos, without_tag=False)

print(keywords)

# w2i = p.get_wordidx_sequence(keywords)
# sequences = [w2i]
#
# MAX_SEQ_LEN = 15    # 임베딩 벡터 크기
# padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')
#
# print(keywords)
# print(sequences)
# print(padded_seqs)
