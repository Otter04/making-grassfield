FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000
# 이 컨테이너의 앱이 5000번 포트를 사용한다.
# 이는 Mac에 포트를 공개하는 명령이 아니다. 공개하는 것은 터미널에 -p를 사용하는 상황

CMD ["python", "app.py"]