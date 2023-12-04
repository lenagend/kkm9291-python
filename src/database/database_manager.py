import os
import time

import mariadb


# 데이터베이스 연결 설정
class DatabaseManager:
    def __init__(self):
        self.connection = self.connect_to_database()

    @staticmethod
    def connect_to_database():
        max_retries = 5
        retry_delay = 5  # 5초 대기

        for attempt in range(max_retries):
            try:
                return mariadb.connect(
                    user=os.getenv("DB_USER"),
                    password=os.getenv("DB_PASSWORD"),
                    host=os.getenv("DB_HOST"),
                    port=int(os.getenv("DB_PORT")),
                    database=os.getenv("DB_NAME")
                )
            except mariadb.Error as e:
                print(f"연결 시도 {attempt + 1}/{max_retries} 실패: {e}")
                time.sleep(retry_delay)
        raise Exception("MariaDB에 연결할 수 없습니다.")

    def create_lotto_draws_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS lotto_draws (
            draw_no INT PRIMARY KEY,
            draw_date DATE,
            total_sell_amount BIGINT,
            first_prize_amount BIGINT,
            first_prize_winners INT,
            bonus_no INT,
            draw_no1 INT,
            draw_no2 INT,
            draw_no3 INT,
            draw_no4 INT,
            draw_no5 INT,
            draw_no6 INT
        );
        """
        self.execute_query(create_table_query)

    def create_recommended_numbers_table(self):
        create_recommended_numbers_table_query = """
        CREATE TABLE IF NOT EXISTS recommended_numbers (
            id INT PRIMARY KEY AUTO_INCREMENT,
            created_at DATE,
            number1 INT,
            number2 INT,
            number3 INT,
            number4 INT,
            number5 INT,
            number6 INT,
            reason TEXT,
            frequency_info TEXT
        );
        """
        self.execute_query(create_recommended_numbers_table_query)

    def execute_query(self, query, params=None, fetch_one=False):
        with self.connection.cursor() as cursor:
            cursor.execute(query, params or ())
            if query.strip().upper().startswith("SELECT"):
                if fetch_one:
                    return cursor.fetchone()
                else:
                    return cursor.fetchall()
            else:
                self.connection.commit()
                return None

    def setup_database(self):
        self.create_lotto_draws_table()
        self.create_recommended_numbers_table()
        self.connection.commit()
        print("데이터베이스 연결 및 테이블 생성 완료")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()
