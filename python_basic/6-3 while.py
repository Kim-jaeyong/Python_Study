# while
costomer = "김재용"
index = 5
while index >= 1:
    print("{0}님 커피가 준비 되었습니다. {1}번 남았어요.".format(costomer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기 처분 되었습니다.")
    
'''
무한루프
index = 1    
while True:
    print("{0}님 커피가 준비 되었습니다. {1}번째 호출 중".format(costomer, index))
    index += 1
'''

index = 5
while index >= 1:
    print("{0}님 커피가 준비 되었습니다. {1}번 남았어요.".format(costomer, index))
    person = input("이름이 어떻게 되세요? : ")
    if person == costomer:
        print("맛있게 드세요")
        break
    else:
     index -= 1
     print("{0}님의 커피입니다. 잠시만 기다려주세요.".format(costomer))
     if index == 0:
        print("커피는 폐기 처분 되었습니다.")
    