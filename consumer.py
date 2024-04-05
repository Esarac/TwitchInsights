from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'spotify-topic',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='spotify-group-1',
    value_deserializer=lambda m: loads(m.decode('utf-8')),
    bootstrap_servers=['localhost:29092']
)

for m in consumer:
    print(m.value)