from utils.CosineSimilarity import Similarity

s = Similarity()
x = s.findAns(sentence1="광주과학고등학교는 어떤 학교인가요?", sentence2="광주과학고등학교는 무슨 학교야?")

print(x)