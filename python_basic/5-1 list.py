# 리스트 []

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨는 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 탔음
subway.append("하하")
print(subway)

# 정형돈씨가 유재석, 조세호 사이에 탔음
subway.insert(1, "정형돈")
print(subway)

# 뒤에서 한명씩 내림
print(subway.pop())
print(subway)

# 같은 사람이 몇명 있는가
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬
num_list = [5, 2, 3, 4, 1]
num_list.sort()
print(num_list)

# 역순
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용 가능
mix_list = ["김재용", 22, True]
print(mix_list)

# 리스트 확장
num_list = [1, 2, 3, 4, 5]
num_list.extend(mix_list)
print(num_list)