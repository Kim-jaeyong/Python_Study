# 객체가 생성될 떄는 __init__함수의 정의된 개수와 동일시 해야함
# ex) marine3 = Unit("마린") -> x hp와 damage를 추가 해야함

class Unit:
    def __init__(self, name, hp, damage): # init은 생성자
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5) # 클래스로부터 만들어지는 것 = 객체
marine2 = Unit("마린", 40, 5) # 이때 마린과 탱크는 Unit 클래스의 인스턴스
tank = Unit("탱크", 150, 35)