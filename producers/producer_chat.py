from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
from decouple import Config, RepositoryEnv
import os
from emoji import demojize
import socket

# Env values
ENV_PATH = os.path.join(os.path.dirname(__file__), '../.env')
env = Config(RepositoryEnv(ENV_PATH))
token = env.get('TW_WEBSOCKET_TOKEN')
kafka_server = env.get('KK_SERVER')

# Kafka create topic (if needed)
# admin_client = KafkaAdminClient(
#     bootstrap_servers="kafka:29092",
#     client_id='messages'
# )

# admin_client.create_topics(new_topics=[NewTopic(name="messages-topic", num_partitions=1, replication_factor=1)], validate_only=False)
# admin_client.close()

# Kafka producer config
producer = KafkaProducer(
    value_serializer=lambda m: m.encode('utf-8'),
    bootstrap_servers=[f'{kafka_server}:29092']
)

# Socket config and connection
config = {
    'server' : 'irc.chat.twitch.tv',
    'port' : 6667,
    'nickname' : 'ScrapingBot',
    'token' : token,
    'channel' : '#knekro',
    # 'channel' : '#Esarac567',
}

sock = socket.socket()
sock.connect((config['server'], config['port']))

sock.send(f"PASS {config['token']}\n".encode('utf-8'))
sock.send(f"NICK {config['nickname']}\n".encode('utf-8'))
sock.send(f"JOIN {config['channel']}\n".encode('utf-8'))

# Get messages
run = True
print('Producer Running!')

while run:
    # run = False
    resp = sock.recv(2048).decode('utf-8')

    if resp.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))
    elif len(resp) > 0:
        producer.send("messages-topic", value=demojize(resp))
        print('~ data sent to "messages-topic"')