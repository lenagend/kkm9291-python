import random


class LottoNumberGenerator:
    def __init__(self, data_accessor):
        self.data_accessor = data_accessor

    @staticmethod
    def generate_pure_random_lotto_numbers(num_sets=10, reason=''):
        """ 순수 랜덤 로또 번호를 생성합니다. """
        pure_random_numbers = []
        for _ in range(num_sets):
            random_set = sorted(random.sample(range(1, 46), 6))
            pure_random_numbers.append((random_set, reason, ""))
        return pure_random_numbers

    def generate_statistical_lotto_numbers(self, last_n_draws=10, num_sets=10, reason="", use_most_frequent=True):
        """ 통계 기반 로또 번호를 생성합니다. """
        draws = self.data_accessor.get_recent_draws(last_n_draws)
        frequency = self.analyze_numbers(draws)

        selected_numbers = self.select_numbers(frequency, 15, top=use_most_frequent)
        lotto_number_sets = []
        for _ in range(num_sets):
            random_set = sorted(random.sample(selected_numbers, 6))
            frequency_info = ", ".join([f"{number}:{frequency[number]}회 출현" for number in random_set])
            lotto_number_sets.append((random_set, reason, frequency_info))

        return lotto_number_sets

    def generate_combined_lotto_numbers(self, num_sets=10):
        """ 순수 랜덤 번호와 다양한 통계 기반 번호를 결합하여 반환합니다. """
        # 순수 랜덤 번호 생성
        random_numbers = self.generate_pure_random_lotto_numbers(num_sets, "6개의 랜덤번호")

        # 통계 기반 번호 생성
        most_frequent_5_draws = self.generate_statistical_lotto_numbers(5, num_sets, "5회동안 가장 자주 나온 번호", True)
        least_frequent_5_draws = self.generate_statistical_lotto_numbers(5, num_sets, "5회동안 가장 적게 나온 번호", False)
        most_frequent_10_draws = self.generate_statistical_lotto_numbers(10, num_sets, "10회동안 가장 자주 나온 번호", True)
        least_frequent_10_draws = self.generate_statistical_lotto_numbers(10, num_sets, "10회동안 가장 적게 나온 번호", False)

        # 모든 번호 결합
        combined_numbers = (random_numbers + most_frequent_5_draws + least_frequent_5_draws +
                            most_frequent_10_draws + least_frequent_10_draws)

        # 결합된 번호를 무작위로 섞음
        random.shuffle(combined_numbers)
        return combined_numbers

    @staticmethod
    def analyze_numbers(draws):
        """ 추첨된 번호들의 빈도를 분석합니다. """
        frequency = {i: 0 for i in range(1, 46)}
        for draw in draws:
            for number in draw:
                frequency[number] += 1
        return frequency

    @staticmethod
    def select_numbers(frequency, num_selections=15, top=True):
        """ 빈도에 따라 번호를 선택합니다. """
        sorted_numbers = sorted(frequency.items(), key=lambda x: x[1], reverse=top)
        return [number for number, _ in sorted_numbers[:num_selections]]
