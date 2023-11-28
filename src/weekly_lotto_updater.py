import schedule
import time
from database.database_manager import conn
from collect_lotto_data import get_lotto_data, save_lotto_data
from generators.lotto_number_saver import generate_and_save_numbers


def fetch_latest_draw_no_from_db():
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(draw_no) FROM lotto_draws")
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else None


def fetch_and_save_next_draw_data():
    latest_draw_no = fetch_latest_draw_no_from_db()
    if latest_draw_no is not None:
        next_draw_no = latest_draw_no + 1
        lotto_data = get_lotto_data(next_draw_no)
        if lotto_data:
            save_lotto_data(lotto_data)
            print(f"{next_draw_no} 회차 데이터를 가져와서 저장했습니다.")

            # 새로운 로또 데이터를 기반으로 추천 번호 생성 및 저장
            generate_and_save_numbers()


def schedule_lotto_update():
    # 매주 일요일 자정에 fetch_and_save_next_draw_data 함수 실행 스케줄링
    schedule.every(10).seconds.do(fetch_and_save_next_draw_data)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    schedule_lotto_update()
