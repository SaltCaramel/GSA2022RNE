from utils.CosineSimilarity import Similarity

s = Similarity()
x = s.findAns(sentence1="도서관은 언제 이용할 수 있어?", sentence2="서울과학고는 어떤 학교야?")

print(x)