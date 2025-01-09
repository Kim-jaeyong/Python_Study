score_file = open("8-3-1score.txt", "w", encoding="utf8") # w는 쓰기모드
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("8-3-1score.txt", "a", encoding="utf8") # a는 append 추가모드
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("8-3-1score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

score_file = open("8-3-1score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

# 파일이 몇줄인지 모를 때
score_file = open("8-3-1score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

score_file = open("8-3-1score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line)
score_file.close()