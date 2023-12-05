import datetime


class LottoDataSaver:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def save_lotto_data(self, data):
        """ API에서 받아온 로또 데이터를 데이터베이스에 저장합니다. """
        if data is None:
            print("API에서 정보를 받아오지 못했습니다.")
            return

        insert_query = """
           INSERT INTO lotto_draws (draw_no, draw_date, total_sell_amount, first_prize_amount, 
           first_prize_winners, bonus_no, draw_no1, draw_no2, draw_no3, draw_no4, draw_no5, draw_no6) 
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

        try:
            self.db_manager.execute_query(insert_query, (
                data['drwNo'], data['drwNoDate'], data['totSellamnt'], data['firstWinamnt'],
                data['firstPrzwnerCo'], data['bnusNo'], data['drwtNo1'], data['drwtNo2'],
                data['drwtNo3'], data['drwtNo4'], data['drwtNo5'], data['drwtNo6']))
            print(f"회차 {data['drwNo']} 저장 완료.")
        except Exception as e:
            print(f"데이터 저장 중 오류 발생: {e}")

    def save_recommended_numbers(self, lotto_numbers):
        """ 추천 로또 번호를 데이터베이스에 저장합니다. """
        for numbers, reason, frequency_info in lotto_numbers:
            insert_query = '''INSERT INTO recommended_numbers (created_at, number1, number2, number3, number4, number5, 
               number6, reason, frequency_info) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            self.db_manager.execute_query(insert_query,
                                          (datetime.datetime.now(), *numbers, reason, frequency_info))

