# 지역변수 전역변수
gun = 10 # 전역변수

'''
def checkPoint(soldiers): # 경계투입
    gun = gun - soldiers
    print("[함수 내]남은 총 갯수 : {}".format(gun))
    
    함수안의 지역변수 gun은 전역변수 gun = 10과 다르기 떄문에 오류 발생
'''

def checkPoint(soldiers): # 경계투입
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내]남은 총 갯수 : {}".format(gun))
    
print("전체 총 : {0}".format(gun))
checkPoint(2) # 2명이 경계 투입을 함
print("남은 총 : {0}".format(gun))

# 하지만 리턴값으로 반환하는 방법이 더 좋은 방법임
def checkPoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

gun = checkPoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))