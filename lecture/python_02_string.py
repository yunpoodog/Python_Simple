# 문자열의 이해(String)
#   활용 예: 데이터 분석, 자연어 처리 응용, 사용자로부터 값 입력받을 때 처리용도

# 1. 문자열 인덱스(index)
#   - 문자열은 각 문자마다 순서(인덱스)가 있음
#   - 첫번째 문자부터 마지막 문자까지 순차적으로 인덱스
#   - 인덱스 시작은 0
#   - 인덱스는 공백 포함
print("=" * 200)
print("Python")

# 2. 문자 추출
#   - 인덱스를 통해서 문자 추출
#   - 인덱스 범위 벗어난 경우 오류
#     (Error: index out of range)
lang = "Python"
print(lang[0])
print(lang[2])
# print(lang[9]) # Error

# -1 인덱스(Reverse Index)
#  - 우측에서 좌측으로 인덱스
#  - 시작값 -1

# 3. 문자열 슬라이싱
#   - lang[3]: 문자 1개만 추출
#   - 부분 문자열 추출하고 싶은 경우
#   - 시작 인덱스, 끝 인덱스 필요
msg = "Python is all you need"
print(msg[0:6]) # 끝 인덱스 +1
print(msg[:6])  # 시작 인덱스 생략 -> 자동 0입력
print(msg[3:])  # 끝 인덱스 생략 -> 자동 -1입력
print(msg[:])   # 처음부터 끝까지

# Quiz
# msg에서 "need"만 추출
# 정방향
print(msg[18:])
# 역방향
print(msg[-4:])

# 4. 문자열 함수
str = "Hello World"

print("=" * 200)
# 4-1. len(): 문자열 길이 계산
print(len(str))

# 4-2. upper() and lower(): 대소문자 변경
#   - 데이터 전처리 -> 1A, 1a -> upper() 1A 통일
print(str.upper())
print(str.lower())

# 4-3. replace(): 문자열 내외 특정 문자 치환
print(str.replace("H", "J"))

# 4-4. split(): 구분자를 기준으로 문자열 분활(Default: 공백)
b = "hello world what a nice weather"
print(b.split) # 거의 이렇게 씀
print(b.split("w")) # 이렇게 잘 안씀

# 4-5. strip(): 문자열의 좌우공백 제거
id = "             python1004             "
print(id)
print(id.strip())

id = "           PyThon1004              "
id.lower() #"          python1004                   "
print(id.lower().strip())   # "python1004" - 여기서 .(~에서)은 참조연산자

# 4-6. find() and rfind(): 문자열 내부의 특정 문자 위치 인덱스 출력
print(str.find("o"))    # Hello^o^ World
print(str.rfind("o"))   # Hello W^o^rld
print(str.find("world"))    # 못찾으면 -1 출력
print(str.find("World"))    # 단어의 첫 글자 인덱스
print(str.rfind("World"))   # 단어의 첫 글자 인덱스

# 4-7. in(): 특정 문자열 포함하는지 확인(Truem False 출력)
print("Hi" in "Hi Python")

# Quiz
id = "cherry1004@gmail.com"

print(id[0:10]) #cherry1004 출력