# 게임에서 같은 유닛이 하나만 만들어지는 경우는 드뭄 그럴떄 같은 유닛을 여러개 생성해내는게 class 붕어빵 틀에 많이 비유하는 편
# 클래스는 하나의 틀 연관이 있는 변수와 함수의 집합

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)