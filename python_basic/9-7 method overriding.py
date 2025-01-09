# 메소드 오버라이딩 : 자식 클래스에서 정의한 메소드를 쓰고 싶을 때 메소드를 새롭게 정의한 후 사용

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
        
# 벌쳐 : 지상 유닛, 기동성 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)
 
# 배틀크루저 : 공중 유닛, 체력 높음, 공격력 높음
battlecrusier = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecrusier.fly(battlecrusier.name, "9시") -> 지상, 공중 유닛 구분해서 fly 와 move로 구분하기 번거로움 
battlecrusier.move("9시")