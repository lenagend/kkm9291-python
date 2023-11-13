from src.lotto_api import get_lotto_data


def main():
    # 1회차 로또 데이터를 가져옵니다.
    lotto_data = get_lotto_data(1043)
    print(lotto_data)


if __name__ == "__main__":
    main()
