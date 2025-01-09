# 문자열 처리 함수
python = "Python is Amazing"

print(python.lower()) # 소문자로
print(python.upper()) # 대문자로
print(python[0].isupper()) # 대문자인가?
print(len(python)) # 문자열 길이
print(python.replace("Python", "Java")) # "Python"을 "Java"로 바꿔줌

index = python.index("n") # n의 위치 찾아줌
print(index)
index = python.index("n", index + 1) # 첫번째 n의 위치 이후의 n의 위치 찾아줌
print(index)

print(python.find("n"))
print(python.find("Java")) # -> "Java"는 없기에 -1 반환
# print(python.index("Java")) -> 오류

print(python.count("n")) # n이 몇번 나왔는지 찾아줌