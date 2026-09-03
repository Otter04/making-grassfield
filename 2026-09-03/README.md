# Docker 이미지와 컨테이너 실습

Python 코드를 담은 Docker 이미지를 만들고, 
하나의 이미지에서 두 개의 컨테이너를 실행한다. 
동일한 이미지를 통해 컨테이너 2개를 실행시킨다. 
=> python을 실행시키기 위한 환경을 담은 이미지 1개를 통해 여러 개의 컨테이너를 만든다. 이때 각 컨테이너는 독립적인 지위를 가진다.

## 실습 명령어

먼저 컨테이너에서 실행시키기 위해 이미지를 만들어야한다.

이미지 만들기:
docker build -t docker-study:1.0 .

첫번째 컨테이너 실행:
docker run --name study-container-1 docker-study:1.0

두번째 컨테이너 실행:
docker run --name study-container-2 -e LEARNER_NAME=Otter docker-study:1.0
=> 참고로 여기서 "LEARNER_NAME=Otter" 을 한 이유는 기존의 main.py 파일에서 변수로 지정해준것을 otter로 지정해주기 위해 작성한거임

현재 실행된 컨테이너 확인:
docker ps -a

### 세부적인 컨테이너 생성 및 실행
위에서 작성한 커맨드들은 처음 생성할 때 작성하는 커맨드이고 내가 실습한 것들은 그저 python 코드를 돌리는 것이기에 계속해서 실행되고 있는 상태는 아니다. 그렇기에 "docker ps" 라고만 커맨드를 작성한다면 실행되고있는 상태가 아니기에 아무것도 뜨지 않는다. 따로 다시 python코드를 실행하고 싶으면 "docker start -a study-container-2" 와 같은 커맨드를 작성하자
