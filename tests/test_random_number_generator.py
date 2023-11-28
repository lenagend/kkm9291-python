import unittest

from src.generators.pure_random_generator import generate_pure_random_lotto_numbers


class TestLottoNumberGenerator(unittest.TestCase):
    def test_pure_random_number_generation(self):
        numbers = generate_pure_random_lotto_numbers()
        self.assertEqual(len(numbers), 30)  # 30개의 세트가 생성되었는지 확인
        for number_set in numbers:
            self.assertEqual(len(number_set), 6)  # 각 세트에 6개의 숫자가 있는지 확인
            self.assertEqual(len(set(number_set)), 6)  # 중복된 숫자가 없는지 확인
            for number in number_set:
                self.assertTrue(1 <= number <= 45)  # 숫자가 1~45 범위에 있는지 확인


if __name__ == '__main__':
    unittest.main()
