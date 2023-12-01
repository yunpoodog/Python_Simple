# TODO: 1. 스케줄링
#       2. 리뷰 중복체크(중복 수집 X)
#       3. DB에 저장된 데이터 Excel 다운로드
#       4. DB에 저장된 데이터 -> 텍스트 분석
#       5. DB에 저장된 데이터 -> WordCloud 시각화

from collect.collect_daum_movie_review import review_collector
def main():
    print("="*100)
    print("== 영화 리뷰 수집기 ==")
    print("="*100)
    movie_code = input("영화 코드>> ")  # 169328
    print("MSG: 매일 12시간에 수집")

    # 중복 리뷰 체크
    # 1. 리뷰 수
    #   - DB에 저장된 리뷰 수(17)
    #   - 현재 수집할 리뷰 수(20)
    #   20 -17 = 3  리뷰 삭제 고려 X!
    # 2. 닐짜 비교
    #   - last_date = DB에 저장된 리뷰 중 가장 최신 날짜 get
    # 수집리뷰_date 비교 last_date
    #
    review_collector(movie_code)

if __name__=="__main__":
    main()