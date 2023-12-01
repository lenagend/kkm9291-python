import requests


class LottoDataCollector:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    @staticmethod
    def get_lotto_data(draw_no):
        """ 주어진 회차 번호에 대한 로또 데이터를 API에서 가져옵니다. """
        url = f"http://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={draw_no}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data.get("returnValue") == "fail":
                return None
            return data
        except Exception as e:
            print(f"API 호출 중 오류 발생: {e}")
            return None


