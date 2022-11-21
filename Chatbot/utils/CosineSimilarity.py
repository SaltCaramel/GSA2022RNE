from konlpy.tag import Komoran
import numpy as np
from numpy import dot


class Similarity:
    # def __init__(self):
    #    print("Success")

    def cos_sim(self, vec1, vec2):
        if np.linalg.norm(vec1) * np.linalg.norm(vec2) == 0:
            return 0.1
        #둘이 곱해서 0이 나온다는 건, 예외처리한 마지막 query의 경우이다. 이게 출력될려면 당연히 0보단 조금 크고 그렇다고 올바른 답 대신 출력할 수는 없으니까 적당히 작은 값을 넣어주었다.

        else :
            return dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

    # 단어 벡터 만들기
    def make_vector(self, tdm):
        vec = []
        for key in tdm:
            vec.append(tdm[key])
        return vec

    def findAns(self, sentence1, sentence2):
        komoran = Komoran()
        bow1 = komoran.nouns(sentence1)
        bow2 = komoran.nouns(sentence2)
        bow = bow1 + bow2
        # 단어 묶음에서 중복제거해 단어 사전 구축
        word_dics = []
        for token in bow:
            if token not in word_dics:
                word_dics.append(token)
        # 하나로 합쳐진 단어 묶음 리스트에서 중복된 단어를 제거해 새로운 단어 사전 리스트를 구축한다.

        # 문장 별 단어 문서 행렬 계산 - 생략 (최적화)
        # 문장 벡터 생성
        vec1 = []
        for word in word_dics:
            if word in bow1:
                vec1.append(1)
            else:
                vec1.append(0)


        vec2 = []
        for word in word_dics:
            if word in bow2:
                vec2.append(1)
            else:
                vec2.append(0)



        doc1 = np.array(vec1)
        doc2 = np.array(vec2)

        # 코사인 유사도 계산
        # 1,2 1,3의 유사도를 보여준다.
        r1 = Similarity.cos_sim(self,vec1=doc1, vec2=doc2)

        return r1


