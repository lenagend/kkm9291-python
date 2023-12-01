class LottoDataAccessor:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get_recent_draws(self, last_n_draws=10):
        """ 최근 추첨된 로또 번호를 데이터베이스에서 가져옵니다. """
        query = '''SELECT draw_no1, draw_no2, draw_no3, draw_no4, draw_no5, draw_no6 
                   FROM lotto_draws
                   ORDER BY draw_date DESC
                   LIMIT ?'''
        return self.db_manager.execute_query(query, (last_n_draws,))

    def fetch_latest_draw_no_from_db(self):
        """ 데이터베이스에서 최신 로또 추첨 번호를 가져옵니다. """
        query = "SELECT COALESCE(MAX(draw_no), 0) FROM lotto_draws"
        result = self.db_manager.execute_query(query, fetch_one=True)
        return result[0] if result else None
