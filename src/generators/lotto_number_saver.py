import datetime
import random

from src.database.database_manager import conn
from src.generators.pure_random_generator import generate_pure_random_lotto_numbers
from src.generators.statistical_number_generator import generate_statistical_lotto_numbers


def save_lotto_numbers(lotto_numbers):
    cursor = conn.cursor()
    for numbers, reason, frequency_info in lotto_numbers:
        cursor.execute('''INSERT INTO recommended_numbers (created_at, number1, number2, number3, number4, number5, 
        number6, reason, frequency_info) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (datetime.datetime.now(), *numbers, reason, frequency_info))
    conn.commit()
    conn.close()


def generate_and_save_numbers():
    # 무작위 번호 생성
    random_lotto_numbers = generate_pure_random_lotto_numbers(num_sets=10)

    # 통계적 번호 생성
    least_frequent_5_draws = generate_statistical_lotto_numbers(last_n_draws=5, num_sets=10,
                                                                base_reason="5회차에서 가장 적게 나온 번호",
                                                                use_most_frequent=False)
    most_frequent_5_draws = generate_statistical_lotto_numbers(last_n_draws=5, num_sets=10,
                                                               base_reason="5회차에서 가장 자주 나온 번호")
    least_frequent_10_draws = generate_statistical_lotto_numbers(last_n_draws=10, num_sets=10,
                                                                 base_reason="10회차에서 가장 적게 나온 번호",
                                                                 use_most_frequent=False)
    most_frequent_10_draws = generate_statistical_lotto_numbers(last_n_draws=10, num_sets=10,
                                                                base_reason="10회차에서 가장 자주 나온 번호")

    all_lotto_numbers = (random_lotto_numbers + least_frequent_5_draws + most_frequent_5_draws + least_frequent_10_draws
                         + most_frequent_10_draws)

    random.shuffle(all_lotto_numbers)

    save_lotto_numbers(all_lotto_numbers)
