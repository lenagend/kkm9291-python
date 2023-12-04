import time
import schedule

from src.database.database_manager import DatabaseManager
from src.collectors.lotto_data_collector import LottoDataCollector
from src.database.lotto_data_accessor import LottoDataAccessor
from src.database.lotto_data_saver import LottoDataSaver
from src.generators.lotto_number_generator import LottoNumberGenerator
from src.updater.weekly_lotto_updater import LottoUpdater


def main():
    with DatabaseManager() as db_manager:
        db_manager.setup_database()

        # 로또 데이터 수집기 인스턴스, 저장 인스턴스 생성 및 실행
        data_collector = LottoDataCollector(db_manager)
        data_accessor = LottoDataAccessor(db_manager)
        number_generator = LottoNumberGenerator(data_accessor)
        data_saver = LottoDataSaver(db_manager)
        updater = LottoUpdater(data_accessor, data_collector, number_generator, data_saver)

        for draw_no in range(1, 1097):
            data = data_collector.get_lotto_data(draw_no)
            if data:
                data_saver.save_lotto_data(data)

        updater.generate_and_save_numbers()
        schedule.every().sunday.at("00:00").do(updater.fetch_and_save_next_draw_data)
        # schedule.every(10).seconds.do(updater.fetch_and_save_next_draw_data)

        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == "__main__":
    main()
