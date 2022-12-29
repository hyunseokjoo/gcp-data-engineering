## Setup Kafka VM

먼저 GCP 환경에서 외부에서 접근 가능한 Compute Instance 하나가 존재 해야 합니다. 만든 하나의 Compute Instance에서 두개의 도커 Container를 올립니다. 하나는 - Eventsim(fake data 생성 모듈), 하나는 - Kafka를 올릴 예정입니다.

- Compute Instance에 SSH connection 접속
  ```bash
  ssh {your_id}@{your_compute_instance_external_ip}
  ```

- Kafka 클러스터 올리기
  ```bash
  sudo apt update && \ 
  sudo apt install -y git && \ 
  cd ~ && \ 
  git clone https://github.com/hyunseokjoo/gcp-data-engineering.git
  ```

- anaconda, docker & docker-compose. 설치하기

  ```bash
  bash ~/gcp-data-engineering/scripts/vm_setup.sh && \
  exec newgrp docker
  ```

- 환경 변수 설정 -
  - the Kafka VM 의 External IP 설정
    ```bash
    export KAFKA_ADDRESS={your_compute_instance_external_ip}
    ```
     **Note**: 위와 같은 경우는 재실행 및 새로 만들 때마다 환경 변수 설정을 해주어야 합니다.

- Kafka 실행하기
  ```bash
  cd ~/gcp-data-engineering/kafka && \
  docker-compose build && \
  docker-compose up -d 
  ```

- Kafka Control Center should port `9021` 로 접속 및 테스트 진행
- Kafka에 eventsim 데이터를 브로커에 보냅니다.
  ```bash
  bash ~/gcp-data-engineering/scripts/eventsim_startup.sh
  ```
  현재 시간부터 24시간까지 100만 사용자에 대한 이벤트 생성이 시작됩니다. 컨테이너는 분리 모드에서 실행됩니다. 진행 상황을 보려면 로그를 봐주세요.

- log 확인하기
  ```bash
  docker logs --follow million_events
  ```
  몇 분안에 메세지가 들어오기 시작합니다. 아래 내 개의 토픽이 보일 것입니다.

  - listen_events
  - page_view_events
  - auth_events
  - status_change_events

- **Note:** eventsim container 재실행시 아래 오류 발생하면 명령어를 실행시켜주세요
  
  >docker: Error response from daemon: Conflict. The container name "/million_events" is already in use by container
  
  ```bash
  docker system prune
  ```