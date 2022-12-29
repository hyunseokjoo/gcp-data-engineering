# Note
아래 내용은 프로젝트와 상관이 없습니다. Kafka폴더로 먼저 이동해주세요.

## Eventsim

Eventsim은 event data를 generate하는 project입니다.(picture something like Spotify); 진짜 데이터 처럼 보이지만 모두 가짜 입니다. repo는 [여기서](https://github.com/Interana/eventsim) 확인 할 수 있습니다. docker image는 [viirya's clone](https://github.com/viirya/eventsim) 에서 확인 가능합니다.

### Setup
아래 명령어를 실행하기 전에 Kafka Cluster가 존재 해야합니다.

#### Docker Image 생성
```bash
docker build -t events:1.0 .
```

#### Kafka로 데이터 보내기
아래 명령어를 실행하면 데이터가 보내집니다.
```bash
docker run -it \
  --network host \
  events:1.0 \
    -c "examples/example-config.json" \
    --start-time "`date +"%Y-%m-%dT%H:%M:%S"`" \
    --end-time "2022-12-31T17:00:00" \
    --nusers 20000 \
    --kafkaBrokerList localhost:9092 \
    --continuous
```