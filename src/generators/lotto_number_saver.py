from src.generators.lotto_number_generator import generate_pure_random_lotto_numbers
from ..database.db_setup import conn


def save_lotto_numbers(lotto_numbers):
    cursor = conn.cursor()
    for numbers in lotto_numbers:
        import datetime
        cursor.execute('''INSERT INTO recommended_numbers (created_at, number1, number2, number3, number4, number5, 
        number6, reason) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                       (datetime.datetime.now(), *numbers, '랜덤생성'))

    conn.commit()


def generate_and_save_numbers():
    lotto_numbers = generate_pure_random_lotto_numbers()
    save_lotto_numbers(lotto_numbers)
