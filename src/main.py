import argparse
import time

import schedule
from dotenv import load_dotenv

from src.database.database_manager import DatabaseManager
from src.collectors.lotto_data_collector import LottoDataCollector
from src.database.lotto_data_accessor import LottoDataAccessor
from src.database.lotto_data_saver import LottoDataSaver
from src.generators.lotto_number_generator import LottoNumberGenerator
from src.updater.weekly_lotto_updater import LottoUpdater


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--env', help='환경 설정 (development 또는 production)', default='development')
    args = parser.parse_args()

    # 환경에 따라 .env 파일 선택
    if args.env == 'production':
        dotenv_path = '../.env.production'
    else:
        dotenv_path = '../.env.development'

    load_dotenv(dotenv_path=dotenv_path)
    with DatabaseManager() as db_manager:
        db_manager.setup_database()

        # 로또 데이터 수집기 인스턴스, 저장 인스턴스 생성 및 실행
        data_collector = LottoDataCollector(db_manager)
        data_accessor = LottoDataAccessor(db_manager)
        number_generator = LottoNumberGenerator(data_accessor)
        data_saver = LottoDataSaver(db_manager)
        updater = LottoUpdater(data_accessor, data_collector, number_generator, data_saver)

        for draw_no in range(1, 20):
            data = data_collector.get_lotto_data(draw_no)
            if data:
                data_saver.save_lotto_data(data)

        # schedule.every().sunday.at("00:00").do(updater.fetch_and_save_next_draw_data)
        schedule.every(5).seconds.do(updater.fetch_and_save_next_draw_data)

        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == "__main__":
    main()
