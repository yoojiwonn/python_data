# import pickle

# with open("profile.pickle","rb") as profile_file: #> 파일을 열어서 profile_file로 이름을 저장해두고, pickle의 로드로 불러서 출력
#     print(pickle.load(profile_file)) #close안해줘서 됨

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r" , encoding="utf8") as study_file:
#     print(study_file.read())

# Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다. 
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다. 

# -x주차 주간보고-
# 부서 :
# 이름 :
# 업무요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt' , '2주차.txt', ... 와 같이 만듭니다. 


# for i in range(1,51):
#     print( str(i)+"주차 보고서 ")
#     report_file = open(str(i)+"주차.txt", "w", encoding="utf8")
#     print("-x주차 주간보고- : ", file=report_file)
#     print("부서 : ", file=report_file)
#     print("이름 : ", file=report_file)
#     print("이름 : ", file=report_file)
#     report_file.close()

# for i in range(1,51):
#     with open(str(i) +"주차 보고서.txt ", "w", encoding="utf8") as report_file:
#         report_file.write("\n- {0} 주차 주간보고- : ".format(i))
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무 요약:")

#class !!
#마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# name = "마린" # 유닛의 이름
# hp = 40
# damage = 5

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1} \n".format(hp, damage))

# #탱크 : 공격 유닛, 탱크 . 포를 쓸 수 있는데 , 일반 모드 / 시즈 모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

# class Unit : 
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다. ".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)
# tank2 = Unit("탱크2", 40, 40)

# #레이스 : 공중유닛, 비행기. 콜로킹 (상대방에서 보이지 않음)
# wraith1 = Unit("레이스",80,5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# #마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 ( 빼앗음 )
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

class Unit: 
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        # print("{0} 유닛이 생성 되었습니다. ".format(self.name))
        # print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

#공격 유닛
class AttackUnit(Unit): ## Unit 을 상속 받음 , damage추가
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
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

    # 파이어뱃 : 공격 유니그 화염방사기
firebat1 = AttackUnit("파이어뱃",50, 16)
firebat1.attack("5시")

    # 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # 상속 2개 
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시") ## flyable에 있는 fly함수를 호출 flyable에는 flying_speed 만 있으니까 이름은 따로 정의  

# method 오버라이딩 :자식 class에서 정의한 메소드를 쓰고 싶을때 