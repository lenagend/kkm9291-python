import mariadb
import sys


try:
    conn = mariadb.connect(
        user="km",
        host="localhost",
        port=3306,
        database="lotto"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# 테이블 생성 쿼리
create_table_query = """
CREATE TABLE IF NOT EXISTS LottoDraws (
    drawNo INT PRIMARY KEY,
    drawDate DATE,
    totalSellAmount BIGINT,
    firstPrizeAmount BIGINT,
    firstPrizeWinners INT,
    bonusNo INT,
    drawNo1 INT,
    drawNo2 INT,
    drawNo3 INT,
    drawNo4 INT,
    drawNo5 INT,
    drawNo6 INT
);
"""

# 테이블 생성 실행
cursor = conn.cursor()
cursor.execute(create_table_query)
conn.commit()
cursor.close()