#파이썬 3일차 
from re import template


# weather = input("오늘 날씨는 어떄요?")
# if weather == "비" or weather == "눈": 
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else: 
#     print("준비물 필요 없어요")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp <30:
#     print("관찮은 날씨에요")
# else:
#     print ("너무 추워요. 나가지 마세요")


#반복문 
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_no in [0,1,2,3,4]:
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))

##while
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

# absent = [2, 5] # 결석
# no_book = [7]
# for student in range(1,11): #1,2,3,4,5,6,7,8,9,10
#     if student in absent:
#         continue # 계속해서 다음 반복을 진행 
#     elif student in no_book :
#         print ("{0}, 책을 읽어봐,  {0}는 교무실로 따라와 ".format(student))
#         break # 반복을 종료
#     print("{0}, 책을 읽어봐".format(student))

# 출석번호가 1,2,3,4, 앞에 100을 붙이기로 함 -> 101,102,103,104
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

#학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I an groot"]
# students = [len(i) for i in students]
# print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

# quiz) 당신은 cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오

# 조건 1 : 승객별 운행 소요시간은 5분 ~ 50분 사이의 난수로 정해집니다. 
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다. 

# 출력문 예제
# 1번쨰 손님 (소요시간 : 15분)
# 2번쨰 손님 (소요시간 : 50분)
# 3번쨰 손님 (소요시간 : 5분)

# 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2분 

# import random 
# pas = 50
# min = random.randrange(5,51) # 5분 부터 50분 사이의 난수 
# if 5 <= min and min <= 50:
#     print min.count()

import random 
## import random 을 하면 ramdom모듈의 함수를
# 쓸때 앞에 random. 함수 형태여야 함 
## 하지만 form random import * 를 하면 함수 앞에 random을 안붙여도됨 
# cnt = 0 # 총 탑승 승객 수 
# for i in range(1,51): # 1~50라는 수 ( 승객 )
#     time = random.randrange(5, 51) # 5분 ~ 50 분 소요 시간
#     if 5 <= time <= 15:
#         print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else:
#         print("[] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
           
# print("총 탑승 승객 : {0} 분".format(cnt))
