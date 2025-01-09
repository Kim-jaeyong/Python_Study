# 딕셔너리(사전)
cabinet = {3:"유재석", 100:"조세호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet)

print(cabinet.get(3))
# print(cabinet[5]) -> X
print(cabinet.get(5))
print(cabinet.get(5, "사용가능"))

print(3 in cabinet)
print(5 in cabinet)

# 새손님
cabinet = {"A-3":"유재석", "B-100":"김태호"}
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간손님
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key와 values 함께 출력
print(cabinet.items())

cabinet.clear()
print(cabinet)
