# 멤버 변수 : 클래스 내에서 정의된 변수

class Unit:
    def __init__(self, name, hp, damage): # init은 생성자
        self.name = name # self.name, self.hp, self.damage는 모두 멤버 변수
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
        
# 레이스 : 공중 유닛, 비행기. 클로킹(상대방에게 보이지 않음)
warith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(warith1.name,warith1.damage))

# 다크아칸의 마인드컨트롤 (상대방 유닛을 내 것으로 빼앗음)
warith2 = Unit("빼앗은 레이스", 80, 5)
warith2.clocking = True # 클래스 내에 없는 변수를 외부에서 추가로 할당

if warith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다".format(warith2.name))
    
# if warith1.clocking == True: warith1은 멤버변수가 name, hp, damage 밖에 없으므로 오류 발생
#     print("{0}는 현재 클로킹 상태입니다.".format(warith1.name))