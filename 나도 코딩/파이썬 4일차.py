
##함수 
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money): # 출금
#     if balance >= money: #잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
#         return balance
# def withdraw_night(balcance, money): #저녁에 출금
#     commission = 100 
#     return commission, balance - money - commission

# open_account()
# balance = 0 
# balance = deposit(balance, 1000)
# balance = withdraw(balance , 2000)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0} 원이며, 잔액은 {1}원 입니다.".format(commission, balance))

# def profile(name, age, main_lang):
#     print("이름: {0}\t나이 : {1}\t주 사용 언어: {2}" \
#         .format(name, age, main_lang)) 

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

#같은 학교 같은 학년 같은 반 같은 수업 
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름: {0}\t나이 : {1}\t주 사용 언어: {2}" \
#         .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이선", age=20) # 순서가 뒤섞여 있어도 잘 전달 됨 
# profile(main_lang="자바", age=25, name="김태호")

# def profile(name, age, *language): ## language의 값이 다를때는 가변 인수를 써서 처리 !
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
# profile("김태호", 25, "kotlin", "Swift")

# gun = 10 

# def checkpoint(soldiers):
#     global gun   # 전역 공간(global)에 있는 gun사용 ( 그냥 gun쓰면 밖에 gun이랑 다른 변수임 ) 일반적으로 잘 쓰진 않음 
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# #checkpoint(2) # 2명이 경계 근무 나감
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))

# quiz) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x 키 (m) x 22
# 여자 : 키(m) x 키 (m) x 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
#     * 함수명 : std_weight
#     * 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다. 

def std_weight(height, gender):
    if gender=="man":
        return height * height * 22
    else :
        return height * height * 21

# height = 175 # cm 단위 
# gender = "man"
# weight = round(std_weight(height/100,gender), 2) # 소수점 둘째 자리까지 출력해줘 
# print("키 {0}cm {1}의 표준 체중은 {2} kg입니다.".format(height, gender, weight))

# 시험 성적
scores = {"수학" : 0, "영어": 50, "코딩":100}
for subject, score in scores.items(): # score에 있는 두개를 가지고 오려면 items 를 써야함 !
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")