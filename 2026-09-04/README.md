# Docker 포트 연결 실습

Python 코드를 담은 Docker 이미지를 만들고,
8000포트와 연결하여 Mac 에서 연결이 가능하도록 만들었다.

## 실습 명령어

docker build -t docker-study-log:1.0 .

docker run -d \
    --name docker-study-log \
    -p 8000:8000 \
    docker-study-log:1.0

