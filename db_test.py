# db_test.py
import mariadb
import sys
from src.db_setup import conn

try:
    # 데이터베이스 연결 시도
    cursor = conn.cursor()

    # LottoDraws 테이블 존재 여부 확인
    cursor.execute("SHOW TABLES LIKE 'LottoDraws';")
    result = cursor.fetchone()
    if result:
        print("데이터베이스에 성공적으로 연결되었습니다.")
        print("LottoDraws 테이블이 존재합니다.")
    else:
        print("LottoDraws 테이블이 존재하지 않습니다.")

    cursor.close()

except mariadb.Error as e:
    print(f"데이터베이스 연결 중 오류 발생: {e}")
    sys.exit(1)

finally:
    # 연결 종료
    conn.close()