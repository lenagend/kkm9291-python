import mariadb
import requests
from database.database_manager import conn


def get_lotto_data(draw_no):
    url = f"http://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={draw_no}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # 응답 코드가 200이 아닌 경우 예외 발생
        data = response.json()
        if data.get("returnValue") == "fail":  # API 응답이 실패했을 때
            return None
        return data
    except Exception as e:
        print(f"API 호출 중 오류 발생: {e}")
        return None


def save_lotto_data(data):
    if data is None:
        print("API에서 정보를 받아오지 못했습니다.")
        return
    cursor = conn.cursor()
    try:
        insert_query = """INSERT INTO lotto_draws (draw_no, draw_date, total_sell_amount, first_prize_amount, 
        first_prize_winners, bonus_no, draw_no1, draw_no2, draw_no3, draw_no4, draw_no5, draw_no6) VALUES (?, ?, ?, 
        ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        cursor.execute(insert_query, (
            data['drwNo'], data['drwNoDate'], data['totSellamnt'], data['firstWinamnt'], data['firstPrzwnerCo'],
            data['bnusNo'], data['drwtNo1'], data['drwtNo2'], data['drwtNo3'], data['drwtNo4'], data['drwtNo5'],
            data['drwtNo6']))
        conn.commit()
        print(f"회차 {data['drwNo']} 저장 완료.")
    except mariadb.Error as e:
        print(f"데이터베이스 쿼리 실행 중 오류 발생: {e}")
    finally:
        cursor.close()


# 데이터 수집 및 저장
if __name__ == "__main__":
    for draw_no in range(1, 1094):  # 예시 범위
        lotto_data = get_lotto_data(draw_no)
        save_lotto_data(lotto_data)
