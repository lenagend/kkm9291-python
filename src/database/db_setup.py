import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="km",
        password="암호",
        host="localhost",
        port=3306,
        database="lotto_test"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)


# LottoDraws 테이블 생성 쿼리
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

# 추천 번호 테이블 생성 쿼리
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
    reason TEXT
);
"""

# 사용자 추천 기록 테이블 생성 쿼리
create_user_recommendations_table_query = """
CREATE TABLE IF NOT EXISTS user_recommendations (
    id INT PRIMARY KEY AUTO_INCREMENT,
    recommendation_id INT,
    created_at DATETIME,
    user_identifier VARCHAR(255),
    FOREIGN KEY (recommendation_id) REFERENCES recommended_numbers(id)
);
"""

# 테이블 생성 실행
cursor = conn.cursor()
cursor.execute(create_table_query)
cursor.execute(create_recommended_numbers_table_query)
cursor.execute(create_user_recommendations_table_query)
# 커밋 (변경 사항 저장)
conn.commit()
# 커서 및 연결 닫기
cursor.close()
