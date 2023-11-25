import random


def generate_pure_random_lotto_numbers():
    """
    순수 랜덤 로또 번호를 생성하는 함수.
    총 30개의 순수 랜덤 번호 세트를 생성한다.
    각 번호 세트는 1부터 45까지의 숫자 중 랜덤으로 선택된 6개의 숫자를 포함한다.
    """
    pure_random_numbers = []

    for _ in range(30):  # 30번 반복
        random_set = sorted(random.sample(range(1, 46), 6))  # 1부터 45까지 숫자 중 무작위로 6개 선택
        pure_random_numbers.append(random_set)

    return pure_random_numbers


# 순수 랜덤 로또 번호 생성 및 출력
pure_random_lotto_numbers = generate_pure_random_lotto_numbers()
print(pure_random_lotto_numbers)
