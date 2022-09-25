#리스트 []

#subway1 = 10
#subway2 = 20
#subway3 = 30

subway = [10,20,30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

#조세호씨가 몇번째 칸에 타고 있는가?
print(subway.index("조세호"))

#하하씨까 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

#정형돈씨를 유재석/조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

#지하철에 있는 사람을 한 명씪 뒤에서 꺼냄
print(subway.pop())
print(subway)

#print(subway.pop())
#print(subway)

#print(subway.pop())
#print(subway)

#같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
#print(subway)
#print(subway.count("유재석"))

##dictionary
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#print(cabinet[5]) #< 오류가 남
print(cabinet.get(5), "사용 가능") #< 오류는 안나고 none값 나옴
print("hi")

##튜플
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

#집합 (set)
#중복 안됨, 순서 없음 
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

#합집합 (java 할 수 있거나 python 할 수 있는 개발자 )
print(java | python)
print(java.union(python))

#python 할 줄 아는 사람이 늘어감 
python.add("김태호")
print(python)

#java를 잊었어요
java.remove("김태호")
print(java)

## 자료 구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))


###퀴즈 3
#댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다. 
#조건 1 : 편의상 댓글은 20명이 작성하였꼬 아이디는 1~ 20 이라고 가정
#조건 2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
#조건 3 : random 모듈의 shuffle과 sample을 활용

print ("-- 당첨자 발표 --")
from collections import UserList
from random import * 
#lst = range(1,21)
#print(list(lst))
#a = sample(lst,1)
#print ("치킨 당첨자 : " + a)
#b = sample(lst,3)
#print ( "커피 당첨자 : " + b)

from random import *
Users = range(1,21)
users = list(Users)

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) #4명 중에서 1명은 치킨, 3명은 커피

print("-- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("--축하합니다 -- ")

