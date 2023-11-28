import random


def generate_pure_random_lotto_numbers(num_sets=10):
    pure_random_numbers = []

    for _ in range(num_sets):  # 30번 반복
        random_set = sorted(random.sample(range(1, 46), 6))  # 1부터 45까지 숫자 중 무작위로 6개 선택
        pure_random_numbers.append((random_set, "6개의 랜덤 번호", ""))

    return pure_random_numbers


# 순수 랜덤 로또 번호 생성 및 출력
pure_random_lotto_numbers = generate_pure_random_lotto_numbers()
