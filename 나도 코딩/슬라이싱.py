jumin = "990120-1234567"
#
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0부터 2 직전까지 
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 (뒤에부터) : " + jumin[-7:])
# 맨 뒤에서 7번째 부터 끝까지 

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1) # 6번째 부터 n의 위치를 찾기 
print(index)

print(python.find("n"))
#print(python.find("Java")) #index로 없는 값을 프린트 할때는 -1을 냄 
#print(python.index("Java"))#index로 없는 값을 프린트 할때는 오류를 냄
print("hi")

print("a" + "b")
print("a", "b")

print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

#print("나는 {age}살이며, {color}색을 좋아해요.".format (color= "빨간", age = 20 ))
#print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20 , color="빨간"))

#age = 20 
#color = "빨간"
#print(f"나는 {age}살이며, {color}색을 좋아해요.")
#\"\" : 문장 내에서 따옴표
print("저는 \"나도코딩\"입니다.")

#\\ : 문장 내에서 \

#\r : 커서를 맨 앞으로 이동 
print("Red Apple\rPine")

#a = "http://naver.com"
#print(a[7:])
#print(a[:4])
#print(a[:3]+a.len + a.count("e") + "!")

#url = "http://naver.com"
url = "http://daum.net"
my_str = url.replace("http://", "") #규칙 1
print(my_str)
my_str = my_str[:my_str.index(".")]# 규칙 2
# my_str[0:5] -> 0~5 직전까지. (0,1,2,3,4)
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.". format(url, password))
