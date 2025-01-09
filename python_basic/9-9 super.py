# super : 상속 받는 부모 클래스를 초기화 할 수 있음

# 일반 유닛
class Unit: # 부모 클래스
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다 [속도 {2}]".format(self.name, location, self.speed))
     
# 공격 유닛   
class AttackUnit(Unit): # 자식 클래스
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 받았습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
       
# 드랍쉽 : 공중 유닛, 수송기. 마린/ 파이어뱃/ 탱크 등을 수송. 공격 불가

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))
        
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드 0
        Flyable.__init__(self, flying_speed)
        
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 건물 
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, location)
        super().__init__(name, hp, 0) 
        self.location = location      

class Example:
    def __init__(self):
        print("Example 생성자")
        
class SuperExample:
    def __init__(self):
        print("SuperExample 생성자")
        
class ExampleSuper(Example, SuperExample):
    def __init__(self):
        super().__init__() # 다중 상속의 경우 맨 첫번째의 부모 클래스 init 함수 호출.
        # Example.__init__(self) # 다중 상속의 부모클래스 모두 호출하고 싶을 경우 super 함수를 두번 써야함
        # SuperExample.__init__(self)
        
ex = ExampleSuper()