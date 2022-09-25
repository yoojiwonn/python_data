# method 오버라이딩 :자식 class에서 정의한 메소드를 쓰고 싶을때 

class Unit: 
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}".format(self.name, location, self.speed))

#공격 유닛
class AttackUnit(Unit): ## Unit 을 상속 받음 , damage추가
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage)) 
        ## 자기 자신의 class의 변수를 받으면 self빼고 변수를 입력하기 

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

#     # 파이어뱃 : 공격 유니그 화염방사기
# firebat1 = AttackUnit("파이어뱃",50, 16)
# firebat1.attack("5시")

#     # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # 상속 2개 
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location): # move 함수 재정의 
        print("[공중 유닛 이동]")
        self.fly(self.name, location) #fly 함수를 가져옴 

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시") ## flyable에 있는 fly함수를 호출 flyable에는 flying_speed 만 있으니까 이름은 따로 정의  


# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음.
battlecruiser = FlyableAttackUnit("배틀 크로저", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")
# method 오버라이딩 :자식 class에서 정의한 메소드를 쓰고 싶을때 < 위와 같이 매번 따로따로 지상유닛인지 공중유닛인지 구분해서 다른 함수를 정의하는게 불편 !

#건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # 아무것도 안하고 일단은 넘어간다는 뜻 

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) 
         # 상속받을때 Unit__init을 써도 되고 , super()을 써두 됨

#서플라이 디폿 : 건물 , 1개 건물 = 8 유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()