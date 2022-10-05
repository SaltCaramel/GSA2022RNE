from konlpy.tag import Komoran
import numpy as np
from numpy import dot


class Similarity:
    # def __init__(self):
    #    print("Success")

    def cos_sim(self, vec1, vec2):
        return dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

    """
    # TDM 만들기 : 단어 문서 행렬
    def make_term_doc_mat(self, sentence_bow, word_dics):
        freq_mat = {}
        for word in word_dics:
            freq_mat[word] = 0

        for word in word_dics:
            if word in sentence_bow:
                freq_mat[word] += 1
        return freq_mat
    """

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

        # 문장 별 단어 문서 행렬 계산
        freq_mat1 = {}
        for word in word_dics:
            freq_mat1[word] = 0

        for word in word_dics:
            if word in bow1:
                freq_mat1[word] += 1

        freq_mat2 = {}
        for word in word_dics:
            freq_mat2[word] = 0

        for word in word_dics:
            if word in bow2:
                freq_mat2[word] += 1


        # 문장 벡터 생성

        vec1 = []
        for key in freq_mat1:
            vec1.append(freq_mat1[key])

        vec2 = []
        for key in freq_mat2:
            vec2.append(freq_mat2[key])

        doc1 = np.array(vec1)
        doc2 = np.array(vec2)

        # 코사인 유사도 계산
        # 1,2 1,3의 유사도를 보여준다.
        r1 = Similarity.cos_sim(self,vec1=doc1, vec2=doc2)

        return r1



