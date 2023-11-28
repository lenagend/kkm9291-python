import os
import argparse

from dotenv import load_dotenv

from src.database.database_manager import DatabaseManager


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


if __name__ == "__main__":
    main()
