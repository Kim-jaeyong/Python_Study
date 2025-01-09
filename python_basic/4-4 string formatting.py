# 문자열 포맷
print("a" + "b")
print("a", "b")

# 방법 1
print("나는 %d살 입니다 " % 22)
print("나는 %s를 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")
print("나는 %s색과 %s색을 좋아해요." % ("빨간", "파란"))

# 방법 2
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("빨간", "파란"))
print("나는 {0}색과 {1}색을 좋아해요".format("빨간", "파란"))
print("나는 {1}색과 {0}색을 좋아해요".format("빨간", "파란"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 22, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 22))

# 방법 4
age = 22
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")