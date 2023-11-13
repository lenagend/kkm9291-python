import requests


def get_lotto_data(draw_no):
    url = f"http://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={draw_no}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # 응답 오류가 있을 경우 예외 발생
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API 요청 중 오류 발생: {e}")
