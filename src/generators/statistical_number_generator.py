import sqlite3
import random
from src.database.database_manager import conn


def get_recent_draws(last_n_draws=10):
    cursor = conn.cursor()
    cursor.execute('''SELECT draw_no1, draw_no2, draw_no3, draw_no4, draw_no5, draw_no6 
                      FROM lotto_draws
                      ORDER BY draw_date DESC
                      LIMIT ?''', (last_n_draws,))

    return cursor.fetchall()


def analyze_numbers(draws):
    frequency = {i: 0 for i in range(1, 46)}
    for draw in draws:
        for number in draw:
            frequency[number] += 1
    return frequency


def select_numbers(frequency, num_selections=15, top=True):
    sorted_numbers = sorted(frequency.items(), key=lambda x: x[1], reverse=top)
    selected_numbers = [number for number, freq in sorted_numbers[:num_selections]]
    return selected_numbers


def generate_statistical_lotto_numbers(last_n_draws=10, num_sets=10, base_reason="", use_most_frequent=True):
    draws = get_recent_draws(last_n_draws)
    frequency = analyze_numbers(draws)

    if use_most_frequent:
        selected_numbers = select_numbers(frequency, num_selections=15, top=True)
    else:
        selected_numbers = select_numbers(frequency, num_selections=15, top=False)

    lotto_number_sets = []
    for _ in range(num_sets):
        random_set = sorted(random.sample(selected_numbers, 6))
        frequency_info = ", ".join([f"{number}:{frequency[number]}회 출현" for number in random_set])
        lotto_number_sets.append((random_set, base_reason, frequency_info))

    return lotto_number_sets


# 각 조건에 대한 10세트의 번호 생성
def printSets():
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

    print("5회차에서 안 나온 랜덤 번호 10세트:", least_frequent_5_draws)
    print("5회차에서 잘 나온 랜덤 번호 10세트:", most_frequent_5_draws)
    print("10회차에서 안 나온 랜덤 번호 10세트:", least_frequent_10_draws)
    print("10회차에서 잘 나온 랜덤 번호 10세트:", most_frequent_10_draws)
