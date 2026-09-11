# Docker 네트워크 : 가상 Edge 장비 상태 대시보드

## 구조
- device-api: 가상 Jetson 상태를 JSON으로 제공
- dashboard: device-api에 요청하고 브라우저 화면에 표시
- edge-lab-net: 두 컨테이너가 통신하는 Docker 네트워크
즉, Mac의 8000번 포트로 들어온 요청을 dashboard 컨테이너의 8000번 포트로 전달한다. 이 상황에서 Flask 웹서버를 통해 상태를 화면에 표시한다. 여기서 말하는 상태는 가상 jetson의 역할을 하는 device-api 컨테이너가 보내는 상태 정보 묶음을 말한다.Docker 내부 네트워크로 두 컨테이너와 연결된 네트워크인 edge-lab-net이 있고 dashboard가 Docker DNS를 통해 device-api의 IP를 찾은 다음(IP는 컨테이너가 생성될 때마다 다르기 때문이다.) 그 컨테이너의 5000번 포트로 요청한다. 컨테이너 내의 가상 jetson 상태 API를 불러와 json형태의 파일을 반환하고 이를 dashboard에 나타낸다.

### Docker DNS?
Docker는 같은 사용자 정의 네트워크(이번 실습에서는 edge-lab-net이다) 안에서 device-api 같은 이름을 IP 로 찾을 수 있게 해준다. 
그렇기에 dashboard는 http://device-api:5000/status 라고 요청할 수 있는거임. 직접 IP를 명시할 필요 없이.


docker network create edge-lab-net
- Docker 내부의 같은 사용자 정의 네트워크 생성(추후 Docker DNS 기능 활용 위한 설정)

docker build -t edge-device-api:1.0 ./device-api
docker build -t edge-dashboard:1.0 ./dashboard

docker run -d --name device-api --network edge-lab-net edge-device-api:1.0

docker run -d --name dashboard --network edge-lab-net -p 8000:8000 \
  -e DEVICE_API_URL=http://device-api:5000/status \
  edge-dashboard:1.0