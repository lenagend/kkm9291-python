# 기본 파이썬 이미지 사용
FROM python:3.12

# 컨테이너 내에서 코드가 실행될 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 나머지 소스 코드 복사
COPY . .

ENV DB_USER=km \
    DB_PASSWORD=Rjawhs11!! \
    DB_HOST=mariadb \
    DB_PORT=3306 \
    DB_NAME=lotto_test

# 애플리케이션 실행 명령
CMD ["python", "./main.py"]
