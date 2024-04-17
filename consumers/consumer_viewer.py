from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'viewers-topic',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='viewers-group-1',
    value_deserializer=lambda m: loads(m.decode('utf-8')),
    bootstrap_servers=['localhost:29092']
)

for m in consumer:
    print('Viewers:')
    for user in m.value['data']:
        print(f"    ~{user['user_name']}")