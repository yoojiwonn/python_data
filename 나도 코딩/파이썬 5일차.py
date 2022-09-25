# print("Python", "Java", sep=",", end="?")
# print("무엇이 더 재밌을 까요 ?") #end를 써주면 프린트 두개해도 됨

#은행 대기 순번표 
# # 001, 002, 003,...
# for num in range(1,21):
#     print("대기번호 :" + str(num).zfill(3)) #3개 만킄의 크기에서 값이 없는 부분은 0으로 채워라 

# answer = input("아무 값이나 입력하세요 :") # input 으로 받는것은 항상 str타입임
# print("입력하신 값은" +answer+ "입니다.")

#빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10 자리 공간을 확보
# print("{0: >10}".format(500))
# #양수일 땐 +로 표시, 음수일 땐 -로 표시 , +10을 쓰면 양수일때 도 + 가 나옴 
# print("{0: >+10}".format(+500)) 
# print("{0: >+10}".format(-500))

# #왼쪽 정렬하고, 빈칸으로_로 채움
# print("{0:_<10}".format(500))

# #3자리 마다 콤마를 찍어주기
# print("{0:,}".format(100000000000))

# #소수점 출력
# print("{0:f}".format(5/3))

# #소수점 특정 자리수 까지만 표시 (소수점 3쨰 자리에서 반올림)
# print("{0:.2f}".format(5/3))

#파일 입출력
#score텍스트 파일을 열고, w함, 꼭 닫아주기 
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

#score파일에 추가하기 
# score_file = open("score.txt","a",encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# # score_file.close()

# #score파일 읽기
# score_file = open("score.txt","r" , encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동 
# print(score_file.readline(), end= "")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()
 
# score_file = open("score.txt", "r", encoding="utf8") 
# lines = score_file.readlines() # list형태로 저장 
# for line in lines: 
#     print(line, end="") 
 
# score_file.close() 
 
# # pickle : 프로그램 상에서 데이터를 파일 형태로 저장을 해줌 
import pickle 
# profile_file = open("profile.pickle", "wb") #pickle을 쓰기 위해서는 항상 b를 써줘야함 
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]} 
# print(profile) 
# pickle.dump(profile, profile_file) # profile 에 있는 정보를 profile_file에 저장 
# profile_file.close() 

profile_file = open("profile.pickle", "rb") # 읽기로 
profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기  (load)
print(profile) 
profile_file.close() 