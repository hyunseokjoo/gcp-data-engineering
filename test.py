from ensurepip import bootstrap
from kafka import KafkaConsumer

# KafkaConsumer(토픽 이름, bootstrap_servers = broker_server주소)
consumer = KafkaConsumer('listen_events', bootstrap_servers = ['localhost:9092'])

# 아래와 같이 작성하면 Consumer로 계속 들어오기 때문에 Loop가 돌게 된다.
for messages in consumer:
    print(messages)