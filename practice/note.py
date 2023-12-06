# len
# 문자열 길이 계산
# upper
# 대문자로 변경하여 출력
# lower
# 소문자로 변경하여 출력
# replace
# 치환하여 출력("A" -> "B")
# split
# 구분자를 기준으로 문자열 분활
# strip
# 좌우 공백 제거
# find, rfind
# 글자의 인덱스 출력
# append
# 리스트 제일 뒤에 값 추가
# insert
# 리스트의 원하는 인덱스에 값 추가
# extend
# 리스트 병합
# remove
# 리스트 내 원소를 값으로 제거
# pop
# 리스트 내 원소를 인덱스로 제거
# index
# 인덱스 출력
# sorted
# 정렬
# set
# 중복값 제거
# key, value
# import
# update
# 딕트와 딕트 병합
# in
# get
# 값 접근(있으면 True 출력, 없으면 False 출력)
# clear
# 딕트 값 초기화
# round
# 자리수만큼 반올림

# a = [95, 1, 3, 55, 27, 45]
# b = sorted(a)   # 디폴트: 오름차순
# c = sorted(a, reverse=True) # 내림차순
# print(b)
# print(c)
#
# b = "hello world what a nice weather"
# print(b.split())
# print(b.split("w"))

# # a와 b를 교환하는 코드
#
# a = input("a :")
# b = int(input("b :")) # 이렇게 해야 int로 바뀜
# print(type(a))
# print(type(b))
# a,b = b,a
# print(f"{b},{a} -> {a},{b}")
# # 원하는 구구단 추출 코드
# a = int(input("원하는 단수를 입력하세요."))
# for b in range(1,10):
#     print(f"{a * b} ", end='') # end='' 줄바꿈 하기 싫으면 이거 추가하면 됩니다.
# print()
# # A, B, C, D, F로 계산하는 프로그램
# # 4.1~4.5 : A
# # 3.6~4.0 : B
# # 3.1~3.5 : C
# # 2.6~3.0 : D
# # 2.5 이하 : F
# a = float(input("당신의 학점은?? "))
# if  4.5>=a>=4.1:
#     print(f"A입니다.")
# elif 4.0>=a>=3.6:
#     print(f"B입니다.")
# elif 3.5>=a>=3.1:
#     print(f"C입니다.")
# elif 3.0>=a>=2.6:
#     print(f"D입니다.")
# else:
#     print(f"F입니다. 자퇴하세요. 븅신아")
#
# # (초등학생, 중학생, 고등학생,학생X) 판별
# a = int(input("나이를 입력하세요."))
# if  a>=20 or a<= 7:
#     print(f"학생이 아닙니다.")
# elif a>=17:
#     print(f"고등학생 입니다.")
# elif a>=14:
#     print(f"중학생 입니다.")
# else:
#     print(f"초등학생 입니다.")
# #소주 판매가능 나이 함수로 만들기
# def soju(a):
#     if a>= 20:
#         print(f"소주 O")
#     else:
#         print(f"소주 X")
# soju(a)
#
#
# # 문제1) 사용자가 입력한 단수를 출력하는 코드 -> 위에
#
# # 문제2) 2단부터 9단까지 출력(중첩 for문)
# for i in range(2, 10):
#     for d in range(1,10):
#         print(f"{i}*{d} = {i*d}")
# # 문제3) list a 의 평균값을 계산하세요.
# a = int(input("몇명의 학생입니까??"))
# c=0
# b = []
# for i in range(0,a):
#     b.insert(i,int(input(f"학생 {i+1} :")))
#     c += b[i]
# print(f"평균값은 {c/a}입니다.")

# 문제4) list b에서 최소값 찾기
# a = []
# for i in range(0, 5):
#     a.append(input(f"list {i+1}의 값은?"))
# b = sorted(a)
# print(f"최솟값은 {b[0]}입니다.")
#
#
# def max1(a):
#     max = a[0]
#     for i in range (0,5):
#         if max <= a[i]:
#             max = a[i]
#         else:
#             continue
#     print(max)
#     return max
# max1(a)
# print(max1(a))
#문제 5) list c의 최소값, 최대값 찾기
# list_c = []
# for i in range(0,5):
#     list_c.append(int(input(f"list의 {i+1}값은?")))
# list_upper = sorted(list_c, reverse = True)
# print(f"최소값은 {list_upper[len(list_upper)-1]}이고 최댓값은 {list_upper[0]}입니다.")


# 문제 6) 버블정렬 만들기
# list_a = []
# a = int(input("몇개를 넣을 건가요?"))
# for i in range(0,a):
#     list_a.append(int(input(f"list의 값 {i+1}의 값은?")))
# def bubble(a,b):
#     for i in range(0, b):
#         for e in range(0, b-1):
#             temp = 0
#             if a[e] > a[e+1]:
#                 temp = a[e]
#                 a[e] = a[e+1]
#                 a[e+1] = temp
#             else:
#                 continue
#     for i in range(0, b):
#         print(f"{a[i]} ", end='')
# bubble(list_a, a)
# 문제 7) 중복값 제거한후 다시 리스트
# a = ["1","46","a", "a", "1", "34r", "sd","sd"]
# b = list(set(a))
# print(b)



#문제 1) 로그인(pw) -> 3번 이상 암호를 틀리면 프로그램 종료
# pw = 1234
# i = 0
# while True:
#     a = int(input("암호를 입력하세요."))
#     if i == 2:
#         print(f"{i+1}번 틀리셨습니다! 프로그램 종료 종료 >.<")
#         i = 0
#         break
#     if a == pw:
#         print("어서오세요.")
#         i = 0
#         break
#     elif a != pw:
#         i+=1
#         print(f"삐용삐용 {i}번 틀렸습니다. 조심하세요!!")
# 문제2) 1~100까지 더해서 총합을 계산하세요.
# c=0
# for i in range(1,101):
#    c+=i
# print(c)
# # 계산기 만들기(함수이용)
# # 함수: 덧셈, 뺄셈, 메인
# from rPtksrlgkatn import sum, cha
# print("=== 덧셈 뺄셈 계 산 기 ! ! ! ! ===")
# a= int(input("첫번째수를 입력해주세요 :"))
# b= int(input("두번째수를 입력해주세요 :"))
# c = input("덧셈 뺄셈을 골라주세요.(+ or -)")
# if c == "+":
#     sum(a,b)
# else:
#     cha(a,b)
# list = {1,2,3,4}
# print(len(list))
temp = ["A", "B", "C", "D", "E"]
for i, alpha in enumerate(temp):
    print(i + 1, alpha)