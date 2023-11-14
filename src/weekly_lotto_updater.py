import schedule
import time
from datetime import datetime, timedelta


def get_next_draw_no(current_date, current_draw_no):
    # 2023년 11월 11일이 1093회차인 것을 기준으로 다음 회차 계산
    base_date = datetime(2023, 11, 11)
    base_draw_no = 1093
    weeks_passed = (current_date - base_date).days // 7
    return base_draw_no + weeks_passed


def fetch_and_save_draw_data():
    current_date = datetime.now()
    next_draw_no = get_next_draw_no(current_date, 1093)
    # 여기에 로또 데이터를 가져오고 데이터베이스에 저장하는 로직 구현
    print(f"회차 {next_draw_no} 데이터를 가져와서 저장합니다.")


# 매주 일요일 자정에 fetch_and_save_draw_data 함수 실행 스케줄링
schedule.every().sunday.at("00:00").do(fetch_and_save_draw_data)

while True:
    schedule.run_pending()
    time.sleep(1)
