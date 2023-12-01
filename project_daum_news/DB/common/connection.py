# 파일시스템: 폴더 또는 디렉토리로 데이터를 저장하는 방법
# 데이터베이스: 데이터를 효율적으로 저장하고 관리해주는 시스템(이론)

# 데이터베이스 관리 시스템(DBMS): 데이터베이스 제품

# ** DBMS 종류
#   1. 관계형 데이터베이스(RDB): 전통적인(스키마:명세서)
#   - ORACLE
#   - MySQL
#   - MariaDB

#   2. NoSQL: New(빅데이터)
#   - MongDB
#   - Redis

# ** DBMS 프로세스
#   - ID와 PW 저장
#   - Pycharm(Python) ----------------------- DB(MongoDB)
#   1. Pycharm과 DB Connection 맺기
#   - IP: 컴퓨터를 접속할 수 있는 주소
#   - PORT: 컴퓨터 내의 프로그램 위치
#   - ID and PW
#   2. SQL을 사용해서 작업(CRUD) 진행
#   - SQL(구조질의어): RDB를 사용하기 위해서는 반드시 사용
#   - RDB(SQL)을 사용, NoSQL(SQL X)
#   CREATE      -> INSERT
#   READ        -> SELECT
#   UPUDATE     -> UPDATE
#   DELETE      -> DELETE

# ** MongoDB 사용방법 2가지
#   1. 직접 설치(Local)
#   - IP, PORT, ID, PW
#   - 장점: 사용 편함, 관리 편함, 커스터마이징 가능
#   - 단점: 설치 과정 복잡, 설정 직접 해야함, 컴퓨터 자원 부족
#   2. MongoDB에서 제공하는 Web Cloud 사용
#   - URL, ID, PW
#   - 장점: 사용 편함, 설치 X, 설정 X, 컴퓨터 자원 X
#   - 단점: 관리 X, 커스터마이징 X

# ** MongoDB 구조
#   설치: MongoDB(DBMS)
#           ㄴ DB(카카오톡)
#                   ㄴ Collection(회원)
#                   ㄴ Collection(톡)
#                   ㄴ Collection(친구)
#                   ㄴ ...
#           ㄴ DB(카카오뱅크)
#                   ㄴ Collection(회원)
#                   ㄴ Collection(계좌)
#                   ㄴ Collection(대출)
#                   ㄴ ...
#           ㄴ DB(카카오페이)
#                   ㄴ ...

# pymongo: Python - MongDB 연결해서 사용
from pymongo import MongoClient

# MongoDB

def conn_mongodb():
    # URL, ID, PW
    DB_ID = "root"  # 상수(전체 대문자로 변수명을 사용)
    DB_PW = "1234"  # 예시) 은행 금리(상수)
    client = MongoClient(f"mongodb+srv://{DB_ID}:{DB_PW}@daumcluster.g4sg5cc.mongodb.net/")  # URL
    db = client["daum"]
    collection = db.get_collection("news")
    return collection