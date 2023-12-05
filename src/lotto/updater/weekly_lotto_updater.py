class LottoUpdater:
    def __init__(self, data_accessor, data_collector, number_generator, data_saver):
        self.data_accessor = data_accessor
        self.data_collector = data_collector
        self.number_generator = number_generator
        self.data_saver = data_saver

    def fetch_and_save_next_draw_data(self):
        """ 다음 회차 로또 데이터를 가져와서 저장합니다. """
        latest_draw_no = self.data_accessor.fetch_latest_draw_no_from_db()
        if latest_draw_no is not None:
            next_draw_no = latest_draw_no + 1
            lotto_data = self.data_collector.get_lotto_data(next_draw_no)
            if lotto_data:
                self.data_saver.save_lotto_data(lotto_data)
                print(f"{next_draw_no} 회차 데이터를 가져와서 저장했습니다.")

                # 추천 번호 생성 및 저장
                self.generate_and_save_numbers()

    def generate_and_save_numbers(self):
        """ 추천 번호를 생성하고 저장합니다. """
        combined_numbers = self.number_generator.generate_combined_lotto_numbers()
        self.data_saver.save_recommended_numbers(combined_numbers)



